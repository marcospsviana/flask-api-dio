from flask_httpauth import passlib
from flask_httpauth.get_password import get_salt, hash_password
from flask_httpauth.HTTPBasicAuth import auth

from models import Users


@auth.verify_token
def verify_token(token):
    return Users.query.filter_by(token=token).first()


@auth.verify_password
def verify_password(username, password):
    user = Users.query.filter_by(username).first()
    if user and passlib.hash.sha256_crypt.verify(password, user.password_hash):
        return user


@auth.hash_password
def hash_pw(username, password):
    salt = get_salt(username)
    return hash_password(password, salt)
