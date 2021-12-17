from dataclasses import dataclass
from typing import List


@dataclass
class Page:
    """Models a Page. Properties of _id, title, parent_page_id, url"""

    _id: str
    title: str
    parent_page_id: str
    url: str

    @classmethod
    def create(cls, resp: dict):
        """create from api json response

        Args:
            resp (dict): raw json response

        Returns:
            Page: Page Object
        """
        title = resp.get("properties").get("title").get("title")[0].get("plain_text")
        return cls(
            resp.get("id"), title, resp.get("parent").get("page_id"), resp.get("url")
        )


@dataclass
class Block:

    _id: str
    _type: str
    text: str

    def __eq__(self, otherBlock):
        return self._type == otherBlock._type

    @staticmethod
    def has_text(block: dict) -> bool:
        """Determine if JSON has text associated

        Args:
            block (dict): JSON for 1 block

        Returns:
            bool: True if there is a text object. Use `cls.get_text`
        """
        text_dict = block[block["type"]]
        # dividers will have an empty dictionary
        if text_dict:
            # empty blocks will have a dictonary with empty value for text key
            if text_dict["text"]:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def get_text(block: dict) -> str:
        """Parse JSON for the plain_text associated. To be used with `cls.has_text`

        Args:
            block (dict): JSON for 1 block

        Returns:
            str: text
        """
        try:
            return block[block["type"]]["text"][0]["plain_text"]
        except KeyError:
            print(f"error on {block}")
            return None

    @classmethod
    def from_api(cls, block: dict):
        text = (
            cls.get_text(block) if cls.has_text(block) else ""
        )  # set the text to empty
        return cls(block["id"], block["type"], text)

    @classmethod
    def for_api(cls, i: int, _type: str):
        # for use with Notion API initialization
        # for customization later
        return cls(i, _type, "")


@dataclass
class FlashCard:

    question: Block
    answer: Block

    @classmethod
    def create(cls, question, answer):
        return cls(question.text, answer.text)
