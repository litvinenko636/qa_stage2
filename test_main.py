from basic_auth import BasicAuth
from tools.json_reader import JsonReader


class TestAuth:
    def test_1(self):
        data = JsonReader("data.json")
        request = BasicAuth(data.get_url(), data.get_username(), data.get_password())
        request.authorization()
        request.get_json()
