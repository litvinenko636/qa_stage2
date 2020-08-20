import pytest
from framework.browser_actions import BrowserActions
from tools.some_tools import random_string
from main_page import MainPage


@pytest.mark.usefixtures('selected_driver', 'data')
def test1(selected_driver, data):

    action = BrowserActions(selected_driver)
    action.url_open(data.get_url())

    page = MainPage(selected_driver)

    page.js_alert_button_click()
    page.js_dialog_accept()

    page.js_confirm_button_click()
    page.js_dialog_accept()

    page.js_alert_prompt_click()
    page.js_prompt_send_text(random_string(10))
    page.js_dialog_accept()

    action.driver_close()
