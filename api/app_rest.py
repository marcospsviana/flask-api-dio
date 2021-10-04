from api.developers_app import DevelopersGet, CreateDeveloper, Developer
from api.users import UserAuth, UserCreate
from flask import Flask
from flask_restful import Api


def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(DevelopersGet, "/desenvolvedores")
    api.add_resource(CreateDeveloper, "/create-dev")
    api.add_resource(Developer, "/desenvolvedores/<int:id>")
    api.add_resource(UserCreate, "/create-user")
    api.add_resource(UserAuth, "/authenticate")

    # db = SQLAlchemy(app)
    # migrate = Migrate(app, db)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
