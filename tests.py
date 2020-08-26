import pytest
from framework.browser_tools.browser_actions import BrowserActions
from main_page import MainPage
from form_page import FormPage


@pytest.mark.usefixtures('data', 'config')
def test1(data, config):

    action = BrowserActions()
    action.url_open(config.get_url())

    main_page = MainPage()
    main_page.here_button_click()

    form_page = FormPage()
    form_page.password_field_input(data.get_password())
    form_page.email_field_input(data.get_email())
    form_page.domain_field_input(data.get_domain())
    form_page.dropdown_field_button_click()
    form_page.dropdown_item_click()
    form_page.accept_terms_check()
    form_page.first_form_button_click()

    form_page.select_random_interests(config.get_num())
    is_file_uploaded = form_page.upload_image(config.get_filepath())
    assert is_file_uploaded == True
    form_page.second_form_button_click()
