import requests
import pytest


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
