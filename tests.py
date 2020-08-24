import pytest
from framework.browser_tools.browser_actions import BrowserActions
from main_page import MainPage


@pytest.mark.usefixtures('data', 'config')
def test1(data, config):

    action = BrowserActions()
    action.url_open(config.get_url())

    page_action = MainPage()
    page_action.here_button_click()
    page_action.password_field_input(data.get_password())