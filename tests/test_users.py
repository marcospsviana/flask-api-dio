import json


def test_login_fail_username(client, db):
    payload = json.dumps({"username": "teste", "password": "teste"})
    assert client.post("/authenticate", data=payload).status_code == 400


def test_login_fail_password(client, db):
    payload = json.dumps({"username": "devpro", "password": "null"})
    assert client.post("/authenticate", data=payload).status_code == 403


def test_user_create(client, db):
    payload = json.dumps({"username": "teste", "passord": "teste"})
    assert client.post("/create-user", data=payload)


def test_user_login_failed(client, db):
    headers = {"content-type": "application/json"}
    payload = json.dumps({"username": "", "password": "pass"})
    assert (
        client.post("/authenticate", headers=headers, data=payload).status_code == 400
    )


def test_user_login_successful(client, db):
    headers = {"content-type": "application/json"}
    payload = json.dumps({"username": "devpro", "password": "devnull"})
    assert (
        client.post("/authenticate", headers=headers, data=payload).status_code == 202
    )
