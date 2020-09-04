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

    def get_item(self, text, num):
        response = requests.get(self.url + "/" + text + "/" + str(num))
        if response.json() != {} and response.json() != []:
            Logger(__name__).write_info("correct json response, status code - " + str(response.status_code))
            JsonImporter(text + '_' + str(num) + '.json', response.json()).write()
            return response.status_code
        elif response.json() == {}:
            Logger(__name__).write_warning("incorrect json response, status code - " + str(response.status_code))
            return response.status_code

    def get_items(self, text):
        response = requests.get(self.url + "/" + text)
        if response.json() != {} and response.json() != []:
            Logger(__name__).write_info("correct json response, status code - " + str(response.status_code))
            JsonImporter(text + '.json', response.json()).write()
            return response.status_code
        elif response.json() == {}:
            Logger(__name__).write_warning("incorrect json response, status code - " + str(response.status_code))
            return response.status_code
