from framework.browser_pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.browser_pages.button import Button


class FeedPageLocators:
    my_page_button = (By.XPATH, "//*[@id='l_pr']")


class FeedPage(BasePage):
    def __init__(self):
        self.my_page_button = FeedPageLocators.my_page_button
        super().__init__()

    def my_page_click(self):
        return Button(self.my_page_button).element_click()
