from src.utils import *


def test_get_key():
    key = get_key("notion")
    assert key
    assert isinstance(key, str)


def test_create_authorization():
    auth = create_authorization("hypothesis")
    assert isinstance(auth, dict)
    assert "Authorization" in auth.keys()
    assert auth.get("Authorization")[:6] == "Bearer"


def test_time():
    """Test might fail at the end of the month"""
    # get today and yesterday in datetime format, func returns ms since epoch
    now = datetime.now()
    yesterday = datetime.fromtimestamp(get_yesterday_in_ms_since_epoch() / 1000)
    assert now.day - yesterday.day == 1, "should be 1 day apart"
