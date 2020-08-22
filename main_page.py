from selenium.webdriver.common.by import By
from framework.base_element import BaseElement
from tools.logger import Logger


class MainPage:
    class Button(BaseElement):
        pass



    # def __init__(self, driver):
    #     self.driver = driver
    #     self.actions = BaseElement(driver)
    #
    # def js_alert_button_click(self):
    #     Logger(__name__).write_info("js_alert_button is clicked")
    #     return self.actions.element_click_by_locator(MainPageLocators.js_alert_button)
    #
    # def js_confirm_button_click(self):
    #     Logger(__name__).write_info("js_confirm_button is clicked")
    #     return self.actions.element_click_by_locator(MainPageLocators.js_confirm_button)
    #
    # def js_alert_prompt_click(self):
    #     Logger(__name__).write_info("js_prompt_button is clicked")
    #     return self.actions.element_click_by_locator(MainPageLocators.js_prompt_button)
