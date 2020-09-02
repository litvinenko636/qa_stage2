from selenium.webdriver.common.by import By
from framework.browser_pages.button import Button
from framework.browser_pages.text_field import TextField


class MainPageLocators:
    title_text = (By.XPATH, "//*[@id='content']/div/h3")


class MainPage:
    @staticmethod
    def get_title():
        return TextField(MainPageLocators.title_text).get_text()