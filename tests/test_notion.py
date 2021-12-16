from src.base_utils.base_api import API
from requests import Response


def test_API():
    api = API("notion")
    assert api.base_url == "https://api.notion.com"
