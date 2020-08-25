from selenium.webdriver.common.by import By
from framework.browser_pages.button import Button
from framework.browser_pages.scroll_bar import ScrollBar
from framework.browser_pages.text_field import TextField


class FormPageLocators:
    password_text_field = (By.XPATH, "//*[@placeholder='Choose Password']")
    email_text_field = (By.XPATH, "//*[@placeholder='Your email']")
    domain_text_field = (By.XPATH, "//*[@placeholder='Domain']")
    accept_terms_checkbox = (By.XPATH, "//*[@class='icon icon-check checkbox__check']")
    dropdown_field_button = (By.XPATH, "//*[@class='dropdown__field']")
    dropdown_item_button = (By.CSS_SELECTOR, "div.dropdown__list > div:nth-child(9)")
    next_button = (By.XPATH, "//*[@class='button--secondary']")


class FormPage:
    @staticmethod
    def password_field_input(text):
        TextField(FormPageLocators.password_text_field).text_field_clear()
        return TextField(FormPageLocators.password_text_field).text_input(text)

    @staticmethod
    def email_field_input(text):
        TextField(FormPageLocators.email_text_field).text_field_clear()
        return TextField(FormPageLocators.email_text_field).text_input(text)

    @staticmethod
    def domain_field_input(text):
        TextField(FormPageLocators.domain_text_field).text_field_clear()
        return TextField(FormPageLocators.domain_text_field).text_input(text)

    @staticmethod
    def accept_terms_check():
        return Button(FormPageLocators.accept_terms_checkbox).element_click()

    @staticmethod
    def dropdown_field_button_click():
        return Button(FormPageLocators.dropdown_field_button).element_click()

    @staticmethod
    def dropdown_item_click():
        return Button(FormPageLocators.dropdown_item_button).element_click()

    @staticmethod
    def next_button_click():
        return Button(FormPageLocators.next_button).element_click()
