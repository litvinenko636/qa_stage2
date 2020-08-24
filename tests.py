import pytest
from framework.browser_actions import BrowserActions
from framework.modal_dialogs import AlertActions
from tools.some_tools import random_string
from main_page import MainPage, MainPageLocators


@pytest.mark.usefixtures('selected_driver', 'data')
def test1(selected_driver, data):
    action = BrowserActions(selected_driver)
    action.url_open(data.get_url())

    page = MainPage(selected_driver)
    page.button_click(MainPageLocators.js_alert_button)

    alert = AlertActions(selected_driver)
    alert.dialog_accept()

    page.button_click(MainPageLocators.js_confirm_button)
    alert.dialog_accept()

    page.button_click(MainPageLocators.js_prompt_button)
    alert.dialog_text_input(random_string(10))
    alert.dialog_accept()

    action.driver_close()
