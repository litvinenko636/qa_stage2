import pytest
from framework.webdriver_singleton import Driver
from tools.json_reader import JsonReader


@pytest.yield_fixture(scope="module")
def selected_driver():
    driver = Driver().connect()
    yield driver


@pytest.yield_fixture(scope="module")
def data():
    json_reader = JsonReader('data.json')
    return json_reader


@pytest.yield_fixture(scope="module")
def config():
    json_reader = JsonReader('config.json')
    return json_reader
