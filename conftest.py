import pytest
from tools.json_reader import JsonReader


@pytest.yield_fixture(scope="module")
def config():
    json_reader = JsonReader('config.json')
    return json_reader
