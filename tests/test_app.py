import json


def test_get_page_post(client, db):
    assert client.post("/").status_code == 404


def test_get_page_get_not_found(client, db):
    assert client.get("/").status_code == 404


def test_page_get(client, db):
    assert (
        client.get(
            "/desenvolvedores",
            headers={"Authorization": "Basic ZGV2dGVzdDp0ZXN0ZQ=="},
            data=json.dumps({}),
        ).status_code
        == 200
    )
