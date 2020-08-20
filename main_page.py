from selenium.webdriver.common.by import By
from framework.base_element import BaseElement


class MainPageLocators:
    pass


class MainPage:
    def __init__(self, driver):
        self.actions = BaseElement(driver)
