from base_utils.base_api import API
from requests import Response


class Notion(API):
    def __init__(self):
        super().__init__()
        self.headers["Notion-Version"] = "2021-08-16"

    def get_page(self, page_id: str) -> Response:
        return self._get(f"/v1/pages/{page_id}")


if __name__ == "__main__":
    notion = Notion()
    r = notion.get_page("96a46207e9b945ddbc5619c8f5f0d6d6")
    r.raise_for_status()
    print(r.json())
