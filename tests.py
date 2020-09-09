import pytest
from framework.browser_tools.browser_actions import BrowserActions
from main_page import MainPage


@pytest.mark.usefixtures('config', 'data')
def test1(config, data):
    action = BrowserActions()
    action.url_open(config.get_url())



    action.driver_close()