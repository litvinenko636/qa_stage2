import requests
from requests.auth import HTTPBasicAuth

from tools.logger import Logger


class BasicAuth:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.auth = HTTPBasicAuth(username, password)
        self.request = None

    def authorization(self):
        Logger(__name__).write_info(self.url)
        self.request = requests.get(url=self.url, auth=self.auth)

    def get_json(self):
        data = self.request.json()
        try:
            Logger(__name__).write_info(data)
            Logger(__name__).write_info('data assertion is correct!')
        except AssertionError:
            Logger(__name__).write_error('data assertion is incorrect')
        return data