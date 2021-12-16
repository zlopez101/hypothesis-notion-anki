import json
import time
from datetime import datetime, timedelta
from urllib.parse import urlencode


def get_yesterday_in_ms_since_epoch() -> str:
    yesterday = datetime.now() - timedelta(1)
    return yesterday.isoformat()


def get_key(api: str) -> str:
    """Return the api key

    Args:
        api (str): api desired. One of ["notion", "anki", "hypothesis"]

    Returns:
        str: api key
    """
    with open("keys.json", "r") as fp:
        data = json.load(fp)
        return data[api]["api-key"]


def create_authorization(api: str) -> dict:
    """Create the authorization

    Args:
        api (str): [description]

    Returns:
        dict: [description]
    """
    key = get_key(api)
    return {"Authorization": f"Bearer {key}"}
