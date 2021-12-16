from src._notion import Notion

notion = Notion()
r = notion.get_page("96a46207e9b945ddbc5619c8f5f0d6d6")
r.raise_for_status()
print(r.json())
