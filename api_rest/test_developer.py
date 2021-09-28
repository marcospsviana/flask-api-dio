import json
from .app_rest import create_app


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
