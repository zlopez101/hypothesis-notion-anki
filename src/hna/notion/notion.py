from typing import Tuple, List
from ..base_utils.base_api import API
from more_itertools import sliding_window

from .models import *


class Notion(API):
    def __init__(self, flash_card_type: tuple = ("heading_3", "divider", "paragraph")):
        super().__init__()
        self.headers["Notion-Version"] = "2021-08-16"  # have to add
        self.flash_card_template = self._create_flash_card_template(flash_card_type)

    @staticmethod
    def _create_flash_card_template(flash_cards: Tuple[str]) -> Tuple[Block]:
        """To find the flash cards on a notion page, we need a template for what the cards will look like.
        This method builds the flash card template based on the default (or provided) style. In the future,
        users could customize their preferred metric.

        Args:
            flash_cards: Tuple[str]: desired flash card sequence

        Returns:
            Tuple[Block]: Flash card template as tuple
        """
        return tuple(Block.for_api(i, t) for i, t in enumerate(flash_cards))

    def get_page(self, page_id: str) -> Page:
        """Returns a Page Object

        Args:
            page_id (str): 32 character string specifying page id

        Returns:
            Page: Page object
        """
        return Page.create(self._get(f"/v1/pages/{page_id}"))

    def get_raw_contents(self, page_id: str) -> dict:
        "debug tool"
        return self._get(f"/v1/blocks/{page_id}/children")["results"]

    def get_page_contents(self, page_id: str) -> List[Block]:
        """Get the children blocks of Page with id: page_id

        Args:
            page_id (str): 32 character string specifying page id

        Returns:
            List[Block]: List containing blocks of page contents
        """
        try:
            blocks = [
                Block.from_api(block)
                for block in self._get(f"/v1/blocks/{page_id}/children")["results"]
            ]
            return blocks
        except KeyError:
            pass

    def detect_flash_card(self, blocks: Tuple[dict]) -> Tuple[dict]:
        """[summary]

        # needs customization

        Args:
            blocks (Tuple[dict]): [description]

        Returns:
            Tuple[dict]: [description]
        """
        if all(
            [
                block == template
                for block, template in zip(
                    blocks,
                    self.flash_card_template,
                )
            ]
        ):
            return FlashCard.create(
                blocks[0], blocks[2]
            )  # still hard coded to only have two values
        else:
            return None

    def find_flash_cards(self, page_id: str) -> List[FlashCard]:
        try:
            blocks = self.get_page_contents(page_id)
        except KeyError:
            pass
        flashcards = []
        for window in sliding_window(blocks, 3):
            card = self.detect_flash_card(window)
            if card:
                flashcards.append(card)
        return flashcards
