import json
import pytest
from app_rest import create_app
from models import Developers, Users, db_session
from model_bakery import baker
from flask import request

@pytest.fixture
def developer(db):
    dev = baker.make(Developers, _quantity=1)
    return dev


@pytest.fixture
def user(db):
    user = baker.make(Users, _quantity=1)
    return user


def test_get_page_post():
    flask_app = create_app()
    response = flask_app.test_client().post("/")
    assert response.status_code == 404


def test_get_page_get_not_found():
    flask_app = create_app()
    response = flask_app.test_client().get("/")
    assert response.status_code == 404


def test_get_page_get():
    flask_app = create_app()
    response = flask_app.test_client().get("/desenvolvedores")
    assert response.status_code == 200


def test_post_desenvolvedor():
    flask_app = create_app()
    response = flask_app.test_client().post(
        "/create-dev", data={"id": None, "name": "ze das uvas", "skills_ids": "1,3"}
    )
    assert response.status_code == 200


def test_get_desenvolvedor_index():
    flask_app = create_app()
    response = flask_app.test_client().get("/desenvolvedores/1")
    assert response.status_code == 200


def test_delete_desenvolvedor_index():
    flask_app = create_app()
    response = flask_app.test_client().delete("/desenvolvedores/1")

    assert response.status_code == 200


def test_desenvolvedor_index_delete_error():
    flask_app = create_app()
    response = flask_app.test_client().delete("/desenvolvedores/b")
    assert response.status_code == 404


def test_desenvolvedor_index_put():
    flask_app = create_app()
    headers = {"content-type": "application/json"}
    payload = json.dumps({"id": 1, "name": "ze das uvas", "skills_ids": "Java"})
    response = flask_app.test_client().put(
        "/desenvolvedores/1", headers=headers, data=payload
    )
    assert response.status_code == 200


def test_user_crete():
    flask_app = create_app()
    headers = {"content-type": "application/json"}
    payload = json.dumps({"id": 1, "username": "ze doidin", "password": "dododepedra"})
    response = flask_app.test_client().post(
        "/create-user", headers=headers, data=payload
    )
    assert response.status_code == 201


def test_user_login_failed():
    flask_app = create_app()
    headers = {"content-type": "application/json"}
    payload = json.dumps({"username": "username", "password": "password"})
    response = flask_app.test_client().post(
        "/authenticate", headers=headers, data=payload
    )
    assert response.status_code == 404


def test_user_login_successful():
    flask_app = create_app()
    headers = {"content-type": "application/json"}
    payload = json.dumps({"username": "marcosviana", "password": "laylaebel"})
    response = flask_app.test_client().post(
        "/authenticate", headers=headers, data=payload
    )
    assert response.status_code == 200
