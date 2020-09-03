from framework.browser_pages.driver_wait import ElementWait
from framework.driver.webdriver_singleton import Driver
from selenium.webdriver.support import expected_conditions as EC


class IFrameTool:
    def __init__(self):
        self.driver = Driver().connect()

    @staticmethod
    def iframe_open(frame_reference):
        return (ElementWait().element_wait()).until(EC.frame_to_be_available_and_switch_to_it(frame_reference))

    def iframe_close(self):
        return self.driver.switch_to.default_content()