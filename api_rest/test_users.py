import json
from .app_rest import create_app
from .models import Users, db_session


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
