from framework.browser_pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.browser_pages.button import Button
from framework.browser_pages.text_field import TextField
from tools.some_tools import user_item_add
from tools.json_reader import JsonReader


class UserPage(BasePage):
    @staticmethod
    def get_post_id(post_id):
        user_post = user_item_add(JsonReader('data.json').get_user_id(), post_id)
        post_locator = (By.XPATH, "//*[@id='post" + user_post + "']")
        attribute = 'data-post-id'
        return TextField(post_locator).get_attribute(attribute)

    @staticmethod
    def set_like(user_post):
        locator = 'div.like_wrap._like_wall' + user_post + ' > div > div.like_btns > a.like_btn.like._like.empty'
        like_locator = (By.CSS_SELECTOR, locator)
        return Button(like_locator).element_click()

    @staticmethod
    def get_photo_id(user_post):
        locator = '#wpt' + user_post + ' > div.page_post_sized_thumbs.clear_fix > a'
        like_locator = (By.CSS_SELECTOR, locator)
        attribute = 'data-post-id'
        photo_id = TextField(like_locator).get_attribute(attribute)
        return photo_id
