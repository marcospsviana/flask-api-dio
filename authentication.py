from flask_httpauth import HTTPBasicAuth
from models import Users, db_session
from passlib.hash import hex_sha256
from decouple import config

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):

    secret = config("SECRET_KEY")
    salt = config("SALT")
    username_hash = hex_sha256.hash(username)
    result = db_session.query(Users).filter(Users.username == username_hash)
    user = {}
    password_hash = secret + password + salt
    for row in result:
        user["username"] = row.username
        print(f"row password {row.password}")
        user["password"] = row.password
    if hex_sha256.verify(password_hash, user["password"]):
        return True
    else:
        return False
