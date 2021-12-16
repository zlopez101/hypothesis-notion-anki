from src._notion import Notion
from requests import Response


def test_API(mock_response):
    api = Notion()
    assert api.base_url == "https://api.notion.com"
