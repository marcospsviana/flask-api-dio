from flask import Flask
from flask_restful import Resource, Api

from desenvolvedores import Desenvolvedores, CreateDesenvolvedor, Desenvolvedor


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Desenvolvedores, '/desenvolvedores')
    api.add_resource(CreateDesenvolvedor, '/create-dev')
    api.add_resource(Desenvolvedor, '/desenvolvedores/<int:id>')

    return app

if __name__ == '__main__':
    create_app().run(debug=True)