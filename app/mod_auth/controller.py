from flask import Blueprint, jsonify
from flask import request
from flask_jwt import JWT
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash
from model import User
from app import app, db

mod_auth = Blueprint('auth', __name__, url_prefix='/api')


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user


def identity(payload):
    return User.query.filter_by(id=payload['identity']).first()


@mod_auth.route('/register', methods=['POST'])
def register():
    data = request.get_json(True);
    user = User(username=data['username'], email=data['email'], password=generate_password_hash(data['password']))
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        return jsonify(message="Email or username not unique"), 400

    return jsonify(message="Account created successfully"), 201

jwt = JWT(app, authenticate, identity)
