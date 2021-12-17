from src.notion.models import Page, Block, FlashCard
import pytest


def test_page(get_json):
    dct = get_json("page")
    page = Page.create(dct)
    assert Page.title == ""
    assert Page._id == ""


def test_block(get_json):
    pass


def test_FlashChard(get_json):
    pass
