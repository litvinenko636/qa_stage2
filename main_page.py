from selenium.webdriver.common.by import By
from framework.browser_pages.button import Button
from framework.browser_pages.text_field import TextField


class MainPageLocators:
    here_button = (By.XPATH, "//*[@class='start__link']")
    password_text_field = (By.XPATH, "//*[@class='input input--blue input--gray']")
    domain_text_field = (By.XPATH, "//*[@class='start__link']")
    email_text_field = (By.XPATH, "//*[@class='start__link']")


class MainPage:
    @staticmethod
    def here_button_click():
        return Button(MainPageLocators.here_button).element_click()

    @staticmethod
    def password_field_input(text):
        TextField(MainPageLocators.password_text_field).text_field_clear()
        return TextField(MainPageLocators.password_text_field).text_input(text)

    @staticmethod
    def domain_field_input(text):
        TextField(MainPageLocators.domain_text_field).text_field_clear()
        return TextField(MainPageLocators.domain_text_field).text_input(text)

    @staticmethod
    def email_field_input(text):
        TextField(MainPageLocators.email_text_field).text_field_clear()
        return TextField(MainPageLocators.email_text_field).text_input(text)
