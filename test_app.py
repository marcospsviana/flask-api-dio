import json
import pytest
from app_rest import create_app
from models import Developers
from model_bakery import baker


@pytest.fixture
def developer(db):
    dev = baker.make(Developers, _quantity=1)
    return dev


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
