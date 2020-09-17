import pytest
from feed_page import FeedPage
from framework.browser_tools.browser_actions import BrowserActions
from auth_page import AuthPage
from framework.browser_tools.vk_api_utils import VKApiUtils
from tools.some_tools import random_string, user_post_add
from user_page import UserPage


@pytest.mark.usefixtures('config', 'data')
def test1(config, data):
    action = BrowserActions()
    action.url_open(config.get_url())

    auth_page = AuthPage()
    auth_page.email_input(data.get_email())
    auth_page.password_input(data.get_password())
    auth_page.login_button_click()

    feed_page = FeedPage()
    feed_page.my_page_click()

    vk_api = VKApiUtils(data.get_token())

    random_text_1 = random_string(10)
    response = vk_api.create_post(random_text_1)

    post_id = response['response']['post_id']
    user_post = user_post_add(data.get_user_id(), post_id)

    user_page = UserPage()
    assert user_page.get_post_id(post_id) == user_post

    photo_info = vk_api.save_wall_image()
    random_text_2 = random_string(10)
    vk_api.edit_post(photo_info, random_text_2, post_id)

    vk_api.create_comment(post_id, random_string(10))
    user_page.set_like(user_post)

    # vk_api.delete_post(post_id)
    # action.driver_close()
