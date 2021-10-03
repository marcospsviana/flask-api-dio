import json
from flask import request
from flask_restful import Resource, http_status_message
from api.models import Developers, Users, db_session
from http import HTTPStatus
from flask_httpauth import HTTPBasicAuth
from passlib.context import CryptContext
# from authentication import verify_password
from decouple import config
from passlib.hash import hex_sha256

auth = HTTPBasicAuth()


@auth.verify_password
def verify(username, password):
    myctx = CryptContext(schemes=["sha256_crypt"])
    result = Users.query.filter(Users.username == username)

    user = {}
    for row in result:
        user["username"] = row.username
        print(f"row password {row.password}")
        user["password"] = row.password
    if myctx.verify(password, user["password"]):
        return user
    else:
        return False



class DevelopersGet(Resource):
    @auth.login_required
    def get(self):
        developers = Developers.query.all()
        developer = [
            {"id": dev.id, "name": dev.name, "skills": dev.skills_ids}
            for dev in developers
        ]
        return developer


class CreateDeveloper(Resource):
    @auth.login_required
    def post(self):
        try:
            data = json.loads(request.data)
            print(f'data name create dev {data["name"]}')
            developers = Developers(name=data["name"], skills_ids=data["skills_ids"])
            developers.save()
            return http_status_message(201), 201
        except Exception as err:
            return {"err": err}


class Developer(Resource):
    @auth.login_required
    def get(self, id):
        try:
            developer = Developers.query.filter_by(id=id).first()
            response = {
                "id": developer.id,
                "name": developer.name,
                "skills": developer.skills_ids,
            }
            return response
        except IndexError:
            return HTTPStatus.NOT_FOUND

    @auth.login_required
    def put(self, id):
        data = json.loads(request.data)

        developer = Developers.query.filter_by(id=id).first()
        if developer is None:
            return HTTPStatus.NOT_FOUND
        if data["name"]:
            developer.name = data["name"]
        if data["skills_ids"]:
            developer.skills_ids = data["skills_ids"]
        db_session.add(developer)
        db_session.commit()
        return HTTPStatus.OK

    def delete(self, id):
        try:
            developer = Developers.query.filter_by(id=id).first()

            if developer:
                developer = db_session.session_factory()
                db_session.remove()
                db_session.commit()
            return HTTPStatus.OK
        except IndexError:
            return HTTPStatus.NOT_FOUND
