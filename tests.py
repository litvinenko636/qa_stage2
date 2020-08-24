import pytest
from framework.browser_actions import BrowserActions
from framework.modal_dialogs import AlertActions
from tools.some_tools import random_string
from main_page import MainPage


@pytest.mark.usefixtures('data')
def test1(data):
    action = BrowserActions()
    action.url_open(data.get_url())

    page = MainPage()
    page.alert_button_click()

    alert = AlertActions()
    alert.dialog_accept()

    page.confirm_button_click()
    alert.dialog_accept()

    page.prompt_button_click()
    alert.dialog_text_input(random_string(10))
    alert.dialog_accept()

    action.driver_close()
