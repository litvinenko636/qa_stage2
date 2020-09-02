from framework.browser_pages.base_element import BaseElement
from framework.browser_pages.driver_wait import ElementWait
from selenium.webdriver.support import expected_conditions as EC


class TextField(BaseElement):
    def text_field_clear(self):
        element = (ElementWait().element_wait()).until(EC.presence_of_element_located(self.locator))
        return element.clear()