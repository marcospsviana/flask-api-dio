import json

from decouple import config
from flask import request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, http_status_message
from passlib.hash import pbkdf2_sha256 
from api.models import Users, db_session

auth = HTTPBasicAuth()


@auth.verify_password
def verify(username, password):
    secret = config("SECRET_KEY")
    result = Users.query.filter(Users.username == username).first()
    user = {}
    password_hash = password
    for row in result:
        user["username"] = row.username
        print(f"row password {row.password}")
        user["password"] = row.password
        if pbkdf2_sha256.verify(password_hash, row.password):
            return True
    return False


class UserCreate(Resource):
    def post(self):
        data = json.loads(request.data)
        try:
            salt = config("SALT")
            secret = config("SECRET_KEY")
            password = str(data["password"])
            username = data["username"]
            password_hash = pbkdf2_sha256.hash(password)
            user = {}

            user_db = db_session.query(Users).filter(Users.username == username)

            for row in user_db:
                user_exist = pbkdf2_sha256.verify(username, row.username)
                if user_exist is not None:
                    return "user already exists", 400

            user = Users(username=username, password=password_hash)
            user.save()
            return http_status_message(201), 201
        except Exception as err:
            return {"error": str(err)}


class UserAuth(Resource):
    def post(self):
        data = json.loads(request.data)

        print(f"data {data}, data type {type(data)}")
        secret = config("SECRET_KEY")
        salt = config("SALT")
        password = data["password"]
        username_hash = data["username"]
        try:
            result = db_session.query(Users).filter(Users.username == username_hash)
            user = {}
            password_hash = password
            print(f"password_hash {password_hash}")
            for row in result:
                user["username"] = row.username
                print(f"row password {row.password}")
                user["password"] = row.password
            if pbkdf2_sha256.verify(password_hash, user["password"]):
                return http_status_message(202), 202
            else:
                return http_status_message(403), 403
        except Exception:
            return http_status_message(400), 400
