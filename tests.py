import pytest
from feed_page import FeedPage
from framework.browser_tools.browser_actions import BrowserActions
from auth_page import AuthPage
from framework.browser_tools.vk_api_utils import VKApiUtils
from tools.some_tools import random_string


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
    vk_api.create_post(random_string(10))

    # action.driver_close()
