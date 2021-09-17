import json

import pytest

from app_rest import create_app
from models import Developers
from desenvolvedores import Skills, return_skill


@pytest.fixture
def get_dev_by_id():
    flask_app = create_app()
    response = flask_app.test_client().get("desenvolvedores/<int:id>")
    return response


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


def test_get_desenvolvedor():
    flask_app = create_app()
    response = flask_app.test_client().get("/desenvolvedores/1")
    skills = return_skill('1,2')
    assert json.loads(response.data) == {
        "id": 1,
        "name": "marcos",
        "skills": skills
    }


def test_post_desenvolvedor():
    flask_app = create_app()
    response = flask_app.test_client().post(
        "/create-dev", data={"id": None, "name": "ze das uvas", "skills_ids": "1,3"}
    )

    assert response.status_code == 200


def test_post_desenvolvedor_index():
    flask_app = create_app()
    response = flask_app.test_client().get("/desenvolvedores/1")
    assert response.status_code == 200


def test_post_desenvolvedor_index_delete():
    flask_app = create_app()
    response = flask_app.test_client().delete(f"/desenvolvedores/{0}")

    assert response.status_code == 200


def test_desenvolvedor_index_delete_error():
    flask_app = create_app()
    response = flask_app.test_client().delete("/desenvolvedores/1000")
    assert json.loads(response.data) == {
        "error": "NOT FOUND",
        "message": "Não foi encontrado nenhum desenvolvedor de id 1000",
    }
