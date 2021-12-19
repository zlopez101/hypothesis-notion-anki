from src.hna.notion.models import Page, Block, FlashCard
import pytest


def test_page(get_json):
    dct = get_json("page")
    page = Page.create(dct)
    assert page.title == "Introduction to Azure Fundamentals"
    assert isinstance(page._id, str)
    assert page.parent_page_id == "4d7ec42e-a2c6-46a7-b3ed-f5137cdeb3e5"


def test_block(get_json):
    pass


def test_FlashChard(get_json):
    pass
