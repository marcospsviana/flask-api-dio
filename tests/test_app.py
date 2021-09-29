def test_get_page_post(client):
    assert client.post("/").status_code == 404


def test_get_page_get_not_found(client):
    assert client.get("/").status_code == 404


def test_get_page_get(client):
    assert (
        client.get(
            "/desenvolvedores", headers={"Authorization": "Basic Y2FtaWxhOmNhbWlsYQ=="}
        ).status_code
        == 200
    )
