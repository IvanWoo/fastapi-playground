import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="package")
def client():
    return TestClient(app)
