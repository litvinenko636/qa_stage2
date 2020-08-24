from selenium import webdriver
from tools.logger import Logger
from enum import Enum


class Browsers(Enum):
    firefox = 'firefox'
    chrome = 'chrome'


class WebDriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == Browsers.firefox.value:
            driver = webdriver.Firefox()
            driver.maximize_window()
            Logger(__name__).write_info("Browser is Firefox")
            return driver
        elif browser_name == Browsers.chrome.value:
            driver = webdriver.Chrome()
            driver.maximize_window()
            Logger(__name__).write_info("Browser is Chrome")
            return driver

        Logger(__name__).write_error("Browser name isn't correct: " + str(browser_name))
