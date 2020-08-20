import requests
from requests.auth import HTTPBasicAuth
from tools.logger import Logger


class BasicAuth:
    def __init__(self, url, username, password):
        self.url = url
        self.auth = HTTPBasicAuth(username, password)
        self.request = None

    def authorization(self):
        Logger(__name__).write_info(self.url)
        self.request = requests.get(url=self.url, auth=self.auth)

    def get_json(self):
        Logger(__name__).write_info(self.request.json())
        return self.request.json()
