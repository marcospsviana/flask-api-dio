import json
from flask import request
from flask_restful import Resource

from models import Developers, db_session
from http import HTTPStatus


def return_skill(id):
    list_ids = id.split(",")
    list_skills = list()
    for id in list_ids:
        skill = Skills(int(id)).name  # .query.filter_by(id=id).first()
        list_skills.append(skill)
    return list_skills


class Desenvolvedores(Resource):
    def get(self):
        developers = Developers.query.all()
        developer = [
            {"id": dev.id, "name": dev.name, "skills": dev.skills_ids}
            for dev in developers
        ]
        return developer


class CreateDesenvolvedor(Resource):
    def post(self):
        try:
            dados = json.loads(request.data)
            developers = Developers()
            developers["name"] = dados["name"]
            developers["skills_ids"] = dados["skills_ids"]
            db_session.save(developers)
            db_session.commit()
            return HTTPStatus.OK
        except Exception:
            return HTTPStatus.BAD_REQUEST


class Desenvolvedor(Resource):
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

    def put(self, id):
        dados = json.loads(request.data)

        developer = Developers.query.filter_by(id=id).first()
        if developer is None:
            return HTTPStatus.NOT_FOUND
        if dados["name"]:
            developer.name = dados["name"]
        if dados["skills_ids"]:
            developer.skills_ids = dados["skills_ids"]
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
