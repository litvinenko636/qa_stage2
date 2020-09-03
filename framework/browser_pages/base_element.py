from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from framework.browser_pages.driver_wait import ElementWait
from tools.logger import Logger
from framework.driver.webdriver_singleton import Driver


class BaseElement:

    def __init__(self, locator):
        self.driver = Driver().connect()
        self.locator = locator

    def _find_element(self):
        return (ElementWait().element_wait()).until(EC.presence_of_element_located(self.locator))

    def _find_elements(self):
        return (ElementWait().element_wait()).until(EC.presence_of_all_elements_located(self.locator))

    def element_click(self):
        Logger(__name__).write_info("button is clicked")
        try:
            element = (ElementWait().element_wait()).until(EC.presence_of_element_located(self.locator))
            element.click()
            return True
        except EC:
            return False

    def get_text(self):
        try:
            element = (ElementWait().element_wait()).until(EC.presence_of_element_located(self.locator))
            element_text = element.text
            Logger(__name__).write_info(element_text + " - item text received")
            return element_text
        except EC:
            Logger(__name__).write_error("cant find text in element")

    def text_input(self, text, *args):
        try:
            Logger(__name__).write_info(text + " - has been sent")
            return self._find_element().send_keys(text, *args)
        except exceptions.TimeoutException:
            Logger(__name__).write_error("incorrect input!")

    def move_to_element(self):
        try:
            element = self._find_element()
            Logger(__name__).write_info("to element move")
            return ActionChains(self.driver).move_to_element(element).perform()
        except exceptions.TimeoutException:
            Logger(__name__).write_error("incorrect move!")