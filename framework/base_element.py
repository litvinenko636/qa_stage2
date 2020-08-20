from selenium.common import exceptions as EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from framework.driver_wait import ElementWait
from tools.logger import Logger


class BaseElement:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return (ElementWait(self.driver).element_wait()).until(EC.presence_of_element_located(locator),
                                                               message=f"Can't find element by locator {locator}")

    def find_elements(self, locator):
        return (ElementWait(self.driver).element_wait()).until(EC.presence_of_all_elements_located(locator),
                                                               message=f"Can't find elements by locator {locator}")

    def element_click_by_locator(self, locator):
        return self.find_element(locator).click()

    @staticmethod
    def element_click(element):
        try:
            Logger(__name__).write_info("Click element")
            return element.click()
        except EC.TimeoutException:
            Logger(__name__).write_error("Incorrect click!")

    def text_input(self, locator, text):
        try:
            Logger(__name__).write_info("Text input")
            return self.find_element(locator).send_keys(text)
        except EC.TimeoutException:
            Logger(__name__).write_error("Incorrect input!")

    def move_to_element(self, locator):
        try:
            element = self.find_element(locator)
            Logger(__name__).write_info("Element move")
            return ActionChains(self.driver).move_to_element(element).perform()
        except EC.TimeoutException:
            Logger(__name__).write_error("Incorrect move!")
