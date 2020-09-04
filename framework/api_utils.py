import requests
from requests.exceptions import HTTPError
from tools.logger import Logger


class APIUtils:
    def __init__(self, url):
        try:
            self.response = requests.get(url)
            self.response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            print('Success!')

    def get_content(self):
        Logger(__name__).write_info(self.response.content)
        return self.response.content

    def get_status_code(self):
        Logger(__name__).write_info(self.response.status_code)
        return self.response.status_code
