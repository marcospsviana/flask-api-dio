import json

from decouple import config
from flask import request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, http_status_message
from passlib.hash import hex_sha256
from api.models import Users, db_session

auth = HTTPBasicAuth()


@auth.verify_password
def verify(username, password):
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
        return user
    else:
        return False


class UserCreate(Resource):
    def post(self):
        data = json.loads(request.data)
        print(f"data  UserCreate {data['username']}")
        try:
            salt = config("SALT")
            secret = config("SECRET_KEY")
            password = secret + str(data["password"]) + salt
            username_hash = hex_sha256.hash(str(data["username"]))
            password_hash = hex_sha256.hash(password)
            user = {}

            user_db = db_session.query(Users).filter(Users.username == username_hash)
            for row in user_db:
                user_exist = hex_sha256.verify(data["username"], row.username)
                if user_exist is not None:
                    return "user already exists", 400
            # user.username = username_hash
            # user.password = password_hash
            user = Users(username=username_hash, password=password_hash)
            user.save()
            return http_status_message(201), 201
        except Exception as err:
            return err


class UserAuth(Resource):
    def post(self):
        data = json.loads(request.data)
        if data == "":
            return http_status_message(403), 403
        print(f"data {data}, data type {type(data)}")
        secret = config("SECRET_KEY")
        salt = config("SALT")
        password = data["password"]
        username_hash = hex_sha256.hash(data["username"])
        try:
            result = db_session.query(Users).filter(Users.username == username_hash)
            user = {}
            password_hash = secret + password + salt
            print(f"password_hash {password_hash}")
            for row in result:
                user["username"] = row.username
                print(f"row password {row.password}")
                user["password"] = row.password
            if hex_sha256.verify(password_hash, user["password"]):
                return http_status_message(200), 200
            else:
                return http_status_message(403), 403
        except Exception:
            return http_status_message(400), 400
