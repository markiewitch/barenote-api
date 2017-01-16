from flask import Blueprint
from flask_jwt import JWT
from werkzeug.security import check_password_hash
from model import User
from app import app

mod_auth = Blueprint('auth', __name__, url_prefix='/api')


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user


def identity(payload):
    return User.query.filter_by(id=payload['identity']).first()


jwt = JWT(app, authenticate, identity)
