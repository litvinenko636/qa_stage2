import requests
from requests.exceptions import HTTPError
from tools.logger import Logger
from tools.json_importer import JsonImporter


class APIUtils:
    def __init__(self, url):
        self.url = url

    def get_status_code(self):
        response = requests.get(self.url)
        Logger(__name__).write_info(response.status_code)
        return response.status_code

    def get_posts(self):
        response = requests.get(self.url + "/posts")
        if response.json() != {} and response.json() != []:
            Logger(__name__).write_info("correct json response")
            JsonImporter('posts.json', response.json()).write()
            return response.json()
        else:
            Logger(__name__).write_info("incorrect json response")
            return False

    def get_post(self, num):
        response = requests.get(self.url + "/posts/" + str(num))
        if response.json() != {} and response.json() != []:
            Logger(__name__).write_info("correct json response")
            JsonImporter('post_' + str(num) + '.json', response.json()).write()
            return response.json()
        else:
            Logger(__name__).write_info("incorrect json response")
            return False

