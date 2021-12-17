import requests
import pytest
import json


class MockResponse:
    def __init__(self, status_code: int):
        self.status_code = status_code

    def json(self):
        return {}


@pytest.fixture
def mock_response(monkeypatch):
    def mock_get():
        return MockResponse(200)

    monkeypatch.setattr(requests, "get", mock_get)


@pytest.fixture(scope="function")
def get_json():
    # fixture as a factory function
    def _get_json(model: str) -> dict:
        with open("tests/models.json", "r") as fp:
            data = json.load(fp)
            return data.get(model)

    return _get_json
