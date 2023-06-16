from fastapi.testclient import TestClient
from unittest import mock

from app.main import app
from app.config.lifespan import q, executor


def test_lifespan():
    # https://stackoverflow.com/questions/75714883/how-to-test-a-fastapi-endpoint-that-uses-lifespan-function
    with mock.patch.object(q, "put") as q_mock_method:
        with mock.patch.object(executor, "submit") as executor_mock_method:
            with TestClient(app) as client:
                q_mock_method.assert_has_calls([mock.call(i) for i in range(5)])
                executor_mock_method.assert_called_once()
