from framework.browser_pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.browser_pages.button import Button
from framework.browser_pages.text_field import TextField


class AuthPageLocators:
    email_text_field = (By.XPATH, "//*[@id='index_email']")
    password_text_field = (By.XPATH, "//*[@id='index_pass']")
    login_button = (By.XPATH, "//*[@id='index_login_button']")


class AuthPage(BasePage):
    def __init__(self):
        self.email = AuthPageLocators.email_text_field
        self.password = AuthPageLocators.password_text_field
        self.login_button = AuthPageLocators.login_button
        super().__init__()

    def email_input(self, text):
        return TextField(self.email).text_input(text)

    def password_input(self, text):
        return TextField(self.password).text_input(text)

    def login_button_click(self):
        return Button(self.login_button).element_click()
