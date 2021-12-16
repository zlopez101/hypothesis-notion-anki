import requests
import time
from datetime import datetime, timedelta

from requests import HTTPError
from base_utils.utils import create_authorization, get_yesterday_in_ms_since_epoch


def get_new_annotations(user: str) -> requests.Response:
    """Request all new annotations for the day for user

    Args:
        user (str): user string supplied by cmd line

    Returns:
        requests.Response: Hypothesis API response
    """
    params = {
        "search_after": get_yesterday_in_ms_since_epoch(),
        "user": user,  # get by user
        "sort": "created",
        "order": "asc",  # otherwise, will sort by dates preceding
    }
    try:
        headers = create_authorization("hypothesis")
        r = requests.get(
            "https://hypothes.is/api/search", params=params, headers=headers
        )
        r.raise_for_status()
        return r
    except HTTPError as requestError:
        pass
    except KeyError as utilError:
        pass
    except Exception as OtherError:
        pass


def sort_annotations(r: requests.Response) -> dict:
    response = r.json()["rows"]  # get the annotations

    pass


if __name__ == "__main__":
    from pprint import pprint

    response = get_new_annotations()
    print(response.status_code)
    print(response.headers)
    pprint(response.json())
