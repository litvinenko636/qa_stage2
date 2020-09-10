from framework.browser_pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.browser_pages.text_field import TextField
from tools.some_tools import post_user_id
from tools.json_reader import JsonReader


class UserPage(BasePage):
    @staticmethod
    def get_post_id(post_id):
        user_post_id = post_user_id(JsonReader('data.json').get_user_id(), post_id)
        post_locator = (By.XPATH, "//*[@id='post" + user_post_id + "']")
        attribute = 'data-post-id'
        return TextField(post_locator).get_attribute(attribute)
