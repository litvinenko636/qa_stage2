from selenium.webdriver.common.by import By
from framework.browser_pages.button import Button


class MainPageLocators:
    here_button = (By.XPATH, "//*[@class='start__link']")


class MainPage:
    @staticmethod
    def here_button_click():
        return Button(MainPageLocators.here_button).element_click()
