from app_rest import create_app
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()


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
