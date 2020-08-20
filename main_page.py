from selenium.webdriver.common.by import By
from framework.base_element import BaseElement
from tools.logger import Logger
from selenium.webdriver.common.alert import Alert
import time


class MainPageLocators:
    js_alert_button = (By.XPATH, "//*[@onclick='jsAlert()']")
    js_confirm_button = (By.XPATH, "//*[@onclick='jsConfirm()']")
    js_prompt_button = (By.XPATH, "//*[@onclick='jsPrompt()']")


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = BaseElement(driver)

    def js_alert_button_click(self):
        Logger(__name__).write_info("js_alert_button is clicked")
        return self.actions.element_click_by_locator(MainPageLocators.js_alert_button)

    def js_confirm_button_click(self):
        Logger(__name__).write_info("js_confirm_button is clicked")
        return self.actions.element_click_by_locator(MainPageLocators.js_confirm_button)

    def js_alert_prompt_click(self):
        Logger(__name__).write_info("js_prompt_button is clicked")
        return self.actions.element_click_by_locator(MainPageLocators.js_prompt_button)

    def js_dialog_accept(self):
        Logger(__name__).write_info("dialog accept button is clicked")
        return Alert(self.driver).accept()

    def js_prompt_send_text(self, text):
        Logger(__name__).write_info(text + " has been sent")
        return Alert(self.driver).send_keys(text)
