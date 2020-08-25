import pytest
from framework.browser_tools.browser_actions import BrowserActions
from main_page import MainPage
from form_page import FormPage


@pytest.mark.usefixtures('data', 'config')
def test1(data, config):

    action = BrowserActions()
    action.url_open(config.get_url())

    main_page= MainPage()
    main_page.here_button_click()

    form_page = FormPage()
    form_page.password_field_input(data.get_password())