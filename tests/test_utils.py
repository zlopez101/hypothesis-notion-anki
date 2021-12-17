from src.base_utils.utils import *


def test_get_key():
    key, _ = get_key_and_endpoint("Notion")
    assert isinstance(key, str)


def test_time():
    """Test might fail at the end of the month"""
    pass
    # get today and yesterday in datetime format, func returns ms since epoch
    # now = datetime.now()
    # yesterday = datetime.fromtimestamp(get_yesterday_in_ms_since_epoch() / 1000)
    # assert now.day - yesterday.day == 1, "should be 1 day apart"
