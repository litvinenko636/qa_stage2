import pytest
from feed_page import FeedPage
from framework.browser_tools.browser_actions import BrowserActions
from auth_page import AuthPage

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

    # action.driver_close()