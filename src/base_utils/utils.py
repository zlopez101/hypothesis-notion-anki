import json
import time
from datetime import datetime, timedelta
from typing import Tuple
from urllib.parse import urlencode


def get_yesterday_in_ms_since_epoch() -> str:
    yesterday = datetime.now() - timedelta(1)
    return yesterday.isoformat()


def get_key_and_endpoint(api: str) -> Tuple[str, str]:
    """Return the api key and endpoint

    Args:
        api (str): one of ["notion", "anki", "hypothesis"]'

    Raises:
        KeyError

    Returns:
        Tuple[str, str]: (key, endpoint)
    """
    try:
        with open("keys.json", "r") as fp:
            data = json.load(fp)
            return data[api].get("api-key"), data[api].get("baseUrl")
    except KeyError:
        raise KeyError('Please select one of ["notion", "anki", "hypothesis"]')
