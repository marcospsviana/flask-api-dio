import json

from decouple import config
from flask import request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, http_status_message
from passlib.context import CryptContext

from api.models import Users, db_session

auth = HTTPBasicAuth()


@auth.verify_password
def verify(username, password):
    myctx = CryptContext(schemes=["sha256_crypt"])
    result = Users.query.filter(Users.username == username)
    user = {}
    for row in result:
        if myctx.verify(password, row.password):
            return True
    return False


class UserCreate(Resource):
    def post(self):
        myctx = CryptContext(schemes=["sha256_crypt"])

        data = json.loads(request.data)
        password = data["password"]
        try:

            password_hash = myctx.hash(password)
            username = str(data["username"])
            user = {}

            user_db = db_session.query(Users).filter(Users.username == username)

            for row in user_db:
                user_exist = myctx.verify(username, row.username)
                if user_exist is not None:
                    return "user already exists", 400

            user = Users(username=username, password=password_hash)
            user.save()
            return http_status_message(201), 201
        except Exception as err:
            return {"error": str(err)}


class UserAuth(Resource):
    def post(self):
        myctx = CryptContext(schemes=["sha256_crypt"])

        data = json.loads(request.data)
        print(f"data {data}, data type {type(data)}")
        secret = config("SECRET_KEY")
        salt = config("SALT")
        password = data["password"]
        username_hash = data["username"]
        try:
            result = db_session.query(Users).filter(Users.username == username_hash)
            user = {}
            for row in result:
                if myctx.verify(password, row.password):
                    return http_status_message(202), 202

            return http_status_message(401), 401
        except Exception as err:
            return {"err": str(err)}

