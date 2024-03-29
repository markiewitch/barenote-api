from flask import Flask, jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy
from . import config

app = Flask(__name__)

app.config.from_object(config)

db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    app.logger.warning("404 on %s" % request.full_path)
    return jsonify(error="Not found"), 404


@app.errorhandler(405)
def not_allowed(error):
    return jsonify(error="Method not allowed"), 405


@app.errorhandler(500)
def internal(error):
    return jsonify(error="Internal error"), 500


# Register submodules
from .mod_auth.controller import mod_auth
app.register_blueprint(mod_auth)

from .mod_note import note_module
app.register_blueprint(note_module)


from .mod_category import category_module
app.register_blueprint(category_module)

with app.app_context():
    # Create the database
    db.create_all()
