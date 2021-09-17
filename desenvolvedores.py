import json
from flask import request
from flask_restful import Resource


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


class Desenvolvedores(Resource):
    def get(self):
        return desenvolvedores


class CreateDesenvolvedor(Resource):
    def post(self):
        try:
            dados = json.loads(request.data)
            desenvolvedores.append(dados)
            return {"success": f'cadastro de {dados["nome"]} realizado com sucesso'}
        except Exception as err:
            return {"error": f"{err}"}


class Desenvolvedor(Resource):
    def get(self, id):
        return desenvolvedores[id]

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
