import pytest
from framework.browser_tools.browser_actions import BrowserActions
from main_page import MainPage


@pytest.mark.usefixtures('data')
def test1(data):

    action = BrowserActions()
    action.url_open(data.get_url())

    page_action = MainPage()
    page_action.here_button_click()