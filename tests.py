import pytest
from framework.browser_tools.browser_actions import BrowserActions
from tools.some_tools import random_string
from main_page import MainPage


@pytest.mark.usefixtures('config', 'data')
def test1(config, data):
    action = BrowserActions()
    action.url_open(config.get_url())

    main_page = MainPage()
    title = main_page.get_title()
    assert title == data.get_title()

    main_page.text_input(random_string(10))
    main_page.all_text_bold()
