from random import randint
from selenium.webdriver.common.by import By
from framework.browser_pages.button import Button
from framework.browser_pages.text_field import TextField
from tools.logger import Logger


class FormPageLocators:
    password_text_field = (By.XPATH, "//*[@placeholder='Choose Password']")
    email_text_field = (By.XPATH, "//*[@placeholder='Your email']")
    domain_text_field = (By.XPATH, "//*[@placeholder='Domain']")
    accept_terms_checkbox = (By.XPATH, "//*[@class='icon icon-check checkbox__check']")
    dropdown_field_button = (By.XPATH, "//*[@class='dropdown__field']")
    dropdown_item_button = (By.CSS_SELECTOR, "div.dropdown__list > div:nth-child(9)")
    first_form_button = (By.XPATH, "//*[@class='button--secondary']")
    unselect_all_checkbox = (By.CSS_SELECTOR, "div.avatar-and-interests__section.avatar-and-interests__interests"
                                              "-section > div > div:nth-child(21) > div > span.checkbox.small")
    upload_button = (By.XPATH, "//*[@class='avatar-and-interests__upload-button']")
    second_form_button = (By.XPATH, "//*[@class='button button--stroked button--white button--fluid']")
    cookie_accept_button = (By.XPATH, "//*[@class='button button--solid button--transparent']")
    close_help_form_button = (By.XPATH, "//*[@class='button button--solid button--blue "
                                        "help-form__send-to-bottom-button']")


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
    def first_form_button_click():
        return Button(FormPageLocators.first_form_button).element_click()

    @staticmethod
    def unselect_all_check():
        return Button(FormPageLocators.unselect_all_checkbox).element_click()

    @staticmethod
    def select_random_interests(num):
        FormPage.unselect_all_check()
        locator_start = "div.avatar-and-interests__section.avatar-and-interests__interests-section > div > div:nth-child("
        locator_end = ") > div > span.checkbox.small"
        for item in range(num):
            item_num = str(randint(1, 20))
            Logger(__name__).write_info(item_num + ' - is selected')
            Button((By.CSS_SELECTOR, locator_start + item_num + locator_end)).element_click()

    @staticmethod
    def upload_image(filepath):
        Button(FormPageLocators.upload_button).element_click()
        return Button(FormPageLocators.upload_button).file_upload(filepath)

    @staticmethod
    def second_form_button_click():
        return Button(FormPageLocators.second_form_button).element_click()

    @staticmethod
    def cookie_accept_button_click():
        return Button(FormPageLocators.cookie_accept_button).element_click()

    @staticmethod
    def close_help_form_button_click():
        return Button(FormPageLocators.close_help_form_button).element_click()
