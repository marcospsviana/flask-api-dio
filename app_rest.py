from flask import Flask
from flask_restful import Api


from developers_app import DevelopersGet, CreateDeveloper, Developer


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(DevelopersGet, "/desenvolvedores")
    api.add_resource(CreateDeveloper, "/create-dev")
    api.add_resource(Developer, "/desenvolvedores/<int:id>")

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
