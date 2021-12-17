from src._notion import Notion
from pprint import pprint

notion = Notion()
cards = notion.find_flash_cards("96a46207e9b945ddbc5619c8f5f0d6d6")
print(cards)
