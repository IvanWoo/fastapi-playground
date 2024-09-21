def test_read_main(client):
    response = client.get("/", params={"token": "jessica"})

    assert response.status_code == 200, response.json()
    assert response.json() == {"message": "Hello Bigger Applications!"}


def test_read_main_bad_token(client):
    response = client.get("/", params={"token": "foo"})

    assert response.status_code == 400, response.json()
    assert response.json() == {"detail": "No jessica token provided"}


def test_api_token(client):
    params = {"token": "jessica"}
    # Test with valid API token
    response = client.get(
        "/items/", headers={"X-API-Key": "fake-super-secret-token"}, params=params
    )
    assert response.status_code == 200, response.json()
    assert isinstance(response.json(), dict)

    # Test with invalid API token
    response = client.get(
        "/items/", headers={"X-API-Key": "invalid-token"}, params=params
    )
    assert response.status_code == 401, response.json()
    assert response.json() == {"detail": "Invalid API Key"}

    # Test without API token
    response = client.get("/items/", params=params)
    assert response.status_code == 401, response.json()
    assert response.json() == {"detail": "Invalid API Key"}
