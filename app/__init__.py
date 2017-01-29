from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

app.config.from_object(config)

db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    return jsonify(error="Not found"), 404


@app.errorhandler(405)
def not_allowed(error):
    return jsonify(error="Method not allowed"), 405


@app.errorhandler(500)
def internal(error):
    return jsonify(error="Internal error"), 500


# Register submodules
from mod_auth.controller import mod_auth
app.register_blueprint(mod_auth)

from mod_note import note_module
app.register_blueprint(note_module)

# Create the database
db.create_all()
