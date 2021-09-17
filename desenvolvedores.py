import json
from flask import request
from flask_restful import Resource
from models import Developers
from enum import Enum

class Skills(Enum):
    python = 1
    django = 2
    flask = 3
    kotlin = 4
    CSharp = 5
    Java = 6
    html = 7
    css = 8
    react = 9
    vuejs = 10

desenvolvedores = [
    {
        "nome": "marcos paulo",
        "skills": ["python", "django", "flask"],
    },
    {
        "nome": "ze das couves",
        "skills": [
            "python",
            "django",
            "flask",
            "kotlin",
            "C#",
            "Java",
            "html",
            "css",
            "react",
            "vuejs",
        ],
    },
]

def return_skill(id):
        list_ids = id.split(',')
        list_skills = list()
        for id in list_ids:
            skill = Skills(int(id)).name # .query.filter_by(id=id).first()
            list_skills.append(skill)
        return list_skills

class Desenvolvedores(Resource):
    def get(self):
        developers = Developers.query.all()
        developer = [{'id': dev.id, 'name': dev.name, 'skills': return_skill(dev.skills_ids)} for dev in developers]
        return developer
    
    




class CreateDesenvolvedor(Resource):
    def post(self):
        try:
            dados = json.loads(request.data)
            desenvolvedores.append(dados)
            return {"success": f'cadastro de {dados["name"]} realizado com sucesso'}
        except Exception as err:
            return {"error": f"{err}"}


class Desenvolvedor(Resource):
    def get(self, id):
        developer = Developers.query.filter_by(id=id).first()
        response = {
            'id': developer.id,
            'name': developer.name,
            'skills': return_skill(developer.skills_ids)
        }
        return response

    def put(self, id):
        try:
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
        except IndexError:
            return {
                "error": "NOT FOUND",
                "message": f"Não foi encontrado nenhum desenvolvedor de id {id}",
            }

    def delete(self, id):
        try:
            dado_dev = desenvolvedores.pop(id)
            return dado_dev
        except IndexError:
            return {
                "error": "NOT FOUND",
                "message": f"Não foi encontrado nenhum desenvolvedor de id {id}",
            }
