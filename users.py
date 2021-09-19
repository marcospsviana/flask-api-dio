import json

from decouple import config
from flask import request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, http_status_message
from passlib.hash import pbkdf2_sha256
from models import Users

auth = HTTPBasicAuth()


class UserCreate(Resource):
    def post(self):
        data = json.loads(request.data)
        username = data['username']
        password = data['password']
        users = Users.query.filter_by(username=username).first()
        if users:
            return http_status_message(400), 400
        salt = config('SALT')
        secret = config('SECRET_KEY')
        username = secret + '_' + username
        password = secret + '_' + password
        username_hash = pbkdf2_sha256.hash(username, salt_size=15)
        password_hash = pbkdf2_sha256.hash(password, salt_size=15)
        user = Users()
        user.username = username_hash
        user.password = password_hash
        user.save()
        return http_status_message(201), 201


class UserAuth(Resource):
    def post(self):
        data = json.loads(request.data)
        secret = config('SECRET_KEY')
        username = secret + '_' + data['username']
        password_secret = secret + '_' + data['password']
        user = Users.query.filter(username == username).first()
        if user and pbkdf2_sha256.verify(password_secret, user.password):
            return data['username']
        else:
            return http_status_message(404), 404
