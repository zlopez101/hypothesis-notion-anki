from typing import List, Tuple
from src.base_utils.base_api import API
from dataclasses import dataclass
from more_itertools import sliding_window


@dataclass
class Block:
    _id: str
    _type: str
    text: str

    @classmethod
    def from_api(cls, block: dict):
        return cls(
            block["id"], block["type"], block[block["type"]]["text"][0]["plain_text"]
        )

    def to_flash_card(self):
        return self.text


@dataclass
class FlashCard:

    question: Block
    answer: Block

    @classmethod
    def create(cls, blocks: List[Block]):
        return cls(*[block.to_flash_card() for block in blocks])


class Notion(API):
    def __init__(self):
        super().__init__()
        self.headers["Notion-Version"] = "2021-08-16"

    def get_page_properties(self, page_id: str) -> dict:
        return self._get(f"/v1/pages/{page_id}")

    def get_page_contents(self, page_id: str) -> dict:
        return self._get(f"/v1/blocks/{page_id}/children")

    @staticmethod
    def detect_flash_card(blocks: Tuple[dict]) -> Tuple[dict]:
        # criteria for flash card Heading 3, divider, paragraph,
        if (
            blocks[0]["type"] == "heading_3"
            and blocks[1]["type"] == "divider"
            and blocks[2]["type"] == "paragraph"
        ):
            blocks = [Block.from_api(block) for block in [blocks[0], blocks[2]]]
            return FlashCard.create(blocks)
        else:
            return None

    def find_flash_cards(self, page_id: str) -> List[FlashCard]:
        try:
            blocks = self.get_page_contents(page_id)["results"]
        except KeyError:
            pass
        flashcards = []
        for window in sliding_window(blocks, 3):
            card = self.detect_flash_card(window)
            if card:
                flashcards.append(card)
        return flashcards
