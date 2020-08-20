from selenium.webdriver.support.ui import WebDriverWait
from tools.json_reader import JsonReader


class ElementWait:
    json = JsonReader('config_file.json')

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def element_wait(self):
        return WebDriverWait(self.driver, self.timeout)
