import json
from pathlib import Path

def test_post_desenvolvedor(client, db):

    payload = json.dumps({"name": "devnull", "skills_ids": ["python", "flask"]})
    assert (
        client.post(
            "/create-dev",
            headers={"Authorization": "Basic ZGV2cHJvOmRldm51bGw="},
            data=payload,
        ).status_code
        == 201
    )


def test_get_desenvolvedor_index(client, db):
    assert (
        client.get(
            "/desenvolvedores/1",
            headers={"Authorization": "Basic ZGV2cHJvOmRldm51bGw="},
        ).status_code
        == 200
    )


def test_delete_desenvolvedor_index(client):
    assert (
        client.delete(
            "/desenvolvedores/1",
            headers={"Authorization": "Basic ZGV2cHJvOmRldm51bGw="},
        ).status_code
        == 200
    )


def test_desenvolvedor_index_delete_error(client):
    assert client.delete("/desenvolvedores/b").status_code == 404


def test_desenvolvedor_index_put(client):
    headers = {"Authorization": "Basic ZGV2cHJvOmRldm51bGw="}
    payload = json.dumps({"id": 1, "name": "ze das uvas", "skills_ids": "Java"})
    assert (
        client.put("/desenvolvedores/1", headers=headers, data=payload).status_code
        == 200
    )
