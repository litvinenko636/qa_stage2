from selenium.webdriver.common.by import By
from framework.button import Button


class MainPageLocators:
    js_alert_button = (By.XPATH, "//*[@onclick='jsAlert()']")
    js_confirm_button = (By.XPATH, "//*[@onclick='jsConfirm()']")
    js_prompt_button = (By.XPATH, "//*[@onclick='jsPrompt()']")


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def button_click(self, locator):
        return Button(self.driver, locator).element_click()
