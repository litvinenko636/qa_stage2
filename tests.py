import pytest
from framework.browser_actions import BrowserActions
from main_page import MainPage


@pytest.mark.usefixtures('selected_driver', 'data')
def test1(selected_driver, data):

    action = BrowserActions(selected_driver)
    action.url_open(data.get_url())

    page = MainPage(selected_driver)

    # action.driver_close()
