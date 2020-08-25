from selenium.webdriver.common.by import By
from framework.browser_pages.text_field import TextField


class FormPageLocators:
    password_text_field = (By.XPATH, "//*[@class='input input--blue input--gray']")
    domain_text_field = (By.XPATH, "//*[@class='start__link']")
    email_text_field = (By.XPATH, "//*[@class='start__link']")


class FormPage:
    @staticmethod
    def password_field_input(text):
        TextField(FormPageLocators.password_text_field).text_field_clear()
        return TextField(FormPageLocators.password_text_field).text_input(text)

    @staticmethod
    def domain_field_input(text):
        TextField(FormPageLocators.domain_text_field).text_field_clear()
        return TextField(FormPageLocators.domain_text_field).text_input(text)

    @staticmethod
    def email_field_input(text):
        TextField(FormPageLocators.email_text_field).text_field_clear()
        return TextField(FormPageLocators.email_text_field).text_input(text)