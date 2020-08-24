from selenium.webdriver.support.ui import WebDriverWait
from framework.driver.webdriver_singleton import Driver
from tools.json_reader import JsonReader


class ElementWait:
    json = JsonReader('config.json')

    def __init__(self):
        self.driver = Driver().connect()
        self.timeout = 10

    def element_wait(self):
        return WebDriverWait(self.driver, self.timeout)
