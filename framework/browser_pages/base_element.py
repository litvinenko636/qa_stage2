from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from framework.browser_pages.driver_wait import ElementWait
from accessify import private
from tools.logger import Logger
from framework.driver.webdriver_singleton import Driver


class BaseElement:

    def __init__(self, locator):
        self.driver = Driver().connect()
        self.locator = locator

    @private
    def find_element(self):
        return (ElementWait().element_wait()).until(EC.presence_of_element_located(self.locator))

    @private
    def find_elements(self):
        return (ElementWait().element_wait()).until(EC.presence_of_all_elements_located(self.locator))

    def element_click(self):
        element = (ElementWait().element_wait()).until(EC.presence_of_element_located(self.locator))
        return element.click()

    def text_input(self, text):
        try:
            Logger(__name__).write_info("Text input")
            return self.find_element(self.locator).send_keys(text)
        except exceptions.TimeoutException:
            Logger(__name__).write_error("Incorrect input!")

    def move_to_element(self):
        try:
            element = self.find_element(self.locator)
            Logger(__name__).write_info("Element move")
            return ActionChains(self.driver).move_to_element(element).perform()
        except exceptions.TimeoutException:
            Logger(__name__).write_error("Incorrect move!")
