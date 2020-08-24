from selenium.webdriver.common.by import By
from framework.button import Button


class MainPageLocators:
    js_alert_button = (By.XPATH, "//*[@onclick='jsAlert()']")
    js_confirm_button = (By.XPATH, "//*[@onclick='jsConfirm()']")
    js_prompt_button = (By.XPATH, "//*[@onclick='jsPrompt()']")


class MainPage:

    def alert_button_click(self):
        return Button(MainPageLocators.js_alert_button).element_click()

    def confirm_button_click(self):
        return Button(MainPageLocators.js_confirm_button).element_click()

    def prompt_button_click(self):
        return Button(MainPageLocators.js_prompt_button).element_click()
