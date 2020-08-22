import pytest
from selenium.webdriver.common.by import By
from framework.browser_actions import BrowserActions
from framework.modal_dialogs import AlertActions
from tools.some_tools import random_string
from main_page import MainPage


class MainPageLocators:
    js_alert_button = (By.XPATH, "//*[@onclick='jsAlert()']")
    js_confirm_button = (By.XPATH, "//*[@onclick='jsConfirm()']")
    js_prompt_button = (By.XPATH, "//*[@onclick='jsPrompt()']")


@pytest.mark.usefixtures('selected_driver', 'data')
def test1(selected_driver, data):

    action = BrowserActions(selected_driver)
    action.url_open(data.get_url())

    MainPage.Button(selected_driver, MainPageLocators.js_alert_button).element_click()

    alert = AlertActions(selected_driver)
    alert.dialog_accept()

    MainPage.Button(selected_driver, MainPageLocators.js_confirm_button).element_click()
    alert.dialog_accept()

    MainPage.Button(selected_driver, MainPageLocators.js_prompt_button).element_click()
    alert.dialog_text_input(random_string(10))
    alert.dialog_accept()

    action.driver_close()
