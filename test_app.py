import json
import pytest
from app_rest import create_app
from flask_httpauth import HTTPBasicAuth
from model_bakery import baker
from models import Developers, Users, db_session


auth = HTTPBasicAuth()


@pytest.fixture
def developer(db):
    dev = baker.make(Developers, _quantity=1)
    return dev


def test_login_fail_username():
    flask_app = create_app()
    payload = json.dumps({"username": "camil", "password": "camila"})
    response = flask_app.test_client().post("/authenticate", data=payload)
    assert response.status_code == 400


def test_login_fail_password():
    flask_app = create_app()
    payload = json.dumps({"username": "camila", "password": "cam"})
    response = flask_app.test_client().post("/authenticate", data=payload)
    assert response.status_code == 403


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
    response = flask_app.test_client().get(
        "/desenvolvedores", headers={"Authorization": "Basic Y2FtaWxhOmNhbWlsYQ=="}
    )
    assert response.status_code == 200


def test_post_desenvolvedor():
    flask_app = create_app()
    response = flask_app.test_client().post(
        "/create-dev", headers={"Authorization": "Basic Y2FtaWxhOmNhbWlsYQ=="}
    )
    print(response.data)
    assert response.status_code == 200


def test_get_desenvolvedor_index():
    flask_app = create_app()
    response = flask_app.test_client().get(
        "/desenvolvedores/1", headers={"Authorization": "Basic Y2FtaWxhOmNhbWlsYQ=="}
    )
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
    headers = {"Authorization": "Basic Y2FtaWxhOmNhbWlsYQ=="}
    payload = json.dumps({"id": 1, "name": "ze das uvas", "skills_ids": "Java"})
    response = flask_app.test_client().put(
        "/desenvolvedores/1", headers=headers, data=payload
    )
    assert response.status_code == 200


def test_user_create():
    users = Users(username="user_nam", password="teste")
    users.save()
    assert users.username == "user_nam"
    user_db = db_session.query(Users).filter(Users.username == users.username)
    user_db.delete()
    db_session.commit()


def test_user_login_failed():
    flask_app = create_app()
    headers = {"content-type": "application/json"}
    payload = json.dumps({"username": "username", "password": "password"})
    response = flask_app.test_client().post(
        "/authenticate", headers=headers, data=payload
    )
    assert response.status_code == 400


def test_user_login_successful():
    flask_app = create_app()
    headers = {"content-type": "application/json"}
    payload = json.dumps({"username": "camila", "password": "camila"})
    response = flask_app.test_client().post(
        "/authenticate", headers=headers, data=payload
    )
    assert response.status_code == 200
