import requests
from .utils import get_key_and_endpoint
from requests import Response


class API:
    def __init__(self):
        self.key, self.base_url = get_key_and_endpoint(self.__class__.__name__)
        self.headers = self.auth_header()

    def auth_header(self) -> dict:
        """returns the authorization header

        Returns:
            dict: auth header
        """
        return {"Authorization": f"Bearer {self.key}"}

    def _get(self, endpoint: str, params: dict = {}) -> Response:
        try:
            return requests.get(
                self.base_url + endpoint, params=params, headers=self.headers
            )
        except:
            print("there was an error!")
