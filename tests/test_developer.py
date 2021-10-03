import json
from pathlib import Path

def test_post_desenvolvedor(client, db):

<<<<<<< HEAD
def test_post_desenvolvedor(client, db):

=======
>>>>>>> 94f1ea30bd90da17b14242862bf049a0b5ab9f9e
    payload = json.dumps({"name": "devnull", "skills_ids": ["python", "flask"]})
    assert (
        client.post(
            "/create-dev",
<<<<<<< HEAD
            headers={"Authorization": "Basic ZGV2dGVzdDpkZXZudWxs"},
=======
            headers={"Authorization": "Basic ZGV2cHJvOmRldm51bGw="},
>>>>>>> 94f1ea30bd90da17b14242862bf049a0b5ab9f9e
            data=payload,
        ).status_code
        == 201
    )


def test_get_desenvolvedor_index(client, db):
    assert (
        client.get(
            "/desenvolvedores/1",
<<<<<<< HEAD
            headers={"Authorization": "Basic ZGV2dGVzdDpkZXZudWxs"},
=======
            headers={"Authorization": "Basic ZGV2cHJvOmRldm51bGw="},
>>>>>>> 94f1ea30bd90da17b14242862bf049a0b5ab9f9e
        ).status_code
        == 200
    )


def test_delete_desenvolvedor_index(client):
    assert (
        client.delete(
            "/desenvolvedores/1",
<<<<<<< HEAD
            headers={"Authorization": "Basic ZGV2dGVzdDpkZXZudWxs"},
=======
            headers={"Authorization": "Basic ZGV2cHJvOmRldm51bGw="},
>>>>>>> 94f1ea30bd90da17b14242862bf049a0b5ab9f9e
        ).status_code
        == 200
    )


def test_desenvolvedor_index_delete_error(client):
    assert client.delete("/desenvolvedores/b").status_code == 404


def test_desenvolvedor_index_put(client):
<<<<<<< HEAD
    headers = {"Authorization": "Basic ZGV2dGVzdDpkZXZudWxs"}
=======
    headers = {"Authorization": "Basic ZGV2cHJvOmRldm51bGw="}
>>>>>>> 94f1ea30bd90da17b14242862bf049a0b5ab9f9e
    payload = json.dumps({"id": 1, "name": "ze das uvas", "skills_ids": "Java"})
    assert (
        client.put("/desenvolvedores/1", headers=headers, data=payload).status_code
        == 200
    )
