import json
from api.models import Users, db_session


def test_login_fail_username(client):
    payload = json.dumps({"username": "camil", "password": "camila"})
    assert client.post("/authenticate", data=payload).status_code == 400


def test_login_fail_password(client):
    payload = json.dumps({"username": "camila", "password": "cam"})
    assert client.post("/authenticate", data=payload).status_code == 403


def test_user_create(client):
    users = Users(username="user_nam", password="teste")
    users.save()
    assert users.username == "user_nam"
    user_db = db_session.query(Users).filter(Users.username == users.username)
    user_db.delete()
    db_session.commit()


def test_user_login_failed(client):
    headers = {"content-type": "application/json"}
    payload = json.dumps({"username": "username", "password": "password"})
    assert (
        client.post("/authenticate", headers=headers, data=payload).status_code == 400
    )


def test_user_login_successful(client):
    headers = {"content-type": "application/json"}
    payload = json.dumps({"username": "camila", "password": "camila"})
    assert (
        client.post("/authenticate", headers=headers, data=payload).status_code == 200
    )
