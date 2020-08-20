import pytest
from framework.browser_actions import BrowserActions
from framework.cookie_tool import CookieTool


@pytest.mark.usefixtures('selected_driver', 'data', 'config')
def test1(selected_driver, data, config):
    action = BrowserActions(selected_driver)
    action.url_open(config.get_url())

    cookie = CookieTool(selected_driver)
    cookie.add_some_cookie("example_key_1", data.get_example_key_1())
    cookie.add_some_cookie("example_key_2", data.get_example_key_2())
    cookie.add_some_cookie("example_key_3", data.get_example_key_3())

    cookie.delete_cookie("example_key_1")

    cookie.add_some_cookie("example_key_3", data.get_alternate_value())
    cookie.get_some_cookie("example_key_3")

    cookie.delete_all_cookies()

    action.driver_close()
