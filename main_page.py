from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from framework.browser_pages.button import Button
from framework.browser_pages.text_field import TextField
from framework.browser_tools.iframe_tool import IFrameTool


class MainPageLocators:
    title_text = (By.XPATH, "//*[@id='content']/div/h3")
    frame = (By.CSS_SELECTOR, "iframe")
    frame_text_area = (By.CSS_SELECTOR, "body")
    bold_text_button = (By.XPATH, "//*[@class='mce-ico mce-i-bold']")


class MainPage:
    @staticmethod
    def get_title():
        return TextField(MainPageLocators.title_text).get_text()

    @staticmethod
    def text_input(text):
        iframe = IFrameTool()
        iframe.iframe_open(MainPageLocators.frame)
        TextField(MainPageLocators.frame_text_area).text_field_clear()
        return TextField(MainPageLocators.frame_text_area).text_input(text)

    @staticmethod
    def all_text_bold():
        TextField(MainPageLocators.frame_text_area).text_input(Keys.CONTROL, 'a')
        iframe = IFrameTool()
        iframe.iframe_close()
        Button(MainPageLocators.bold_text_button).element_click()
