from src.hna.notion.notion import Notion
from requests import Response
from src.hna.notion.models import Block


def test_API(mock_response):
    # default settings
    api = Notion()
    assert api.base_url == "https://api.notion.com"
    card_template = api.flash_card_template
    assert isinstance(card_template, tuple)
    assert isinstance(card_template[0], Block)
    assert card_template[0]._type == "heading_3"

    # custom settings for flash cards
    api = Notion(flash_card_type=("heading_1", "paragraph", "paragraph"))
    assert api.flash_card_template[0]._type == "heading_1"
