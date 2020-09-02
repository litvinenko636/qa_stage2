import pytest
from framework.browser_tools.browser_actions import BrowserActions
from main_page import MainPage


@pytest.mark.usefixtures('config')
def test1(config):
    action = BrowserActions()
    action.url_open(config.get_url())
