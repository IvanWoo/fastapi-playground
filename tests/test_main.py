def test_read_main(client):
    response = client.get("/", params={"token": "jessica"})

    assert response.status_code == 200, response.json()
    assert response.json() == {"message": "Hello Bigger Applications!"}


def test_read_main_bad_token(client):
    response = client.get("/", params={"token": "foo"})

    assert response.status_code == 400, response.json()
    assert response.json() == {"detail": "No jessica token provided"}
