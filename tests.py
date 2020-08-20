import pytest
from framework.browser_actions import BrowserActions


@pytest.mark.usefixtures('selected_driver', 'data', 'config')
def test1(selected_driver, data, config):

    action = BrowserActions(selected_driver)
    action.url_open(config.get_url())

    # action.driver_close()
