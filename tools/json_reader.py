import json


class JsonReader:
    def __init__(self, filename):
        self.json_file = open(filename, encoding='utf8')
        self.data = json.load(self.json_file)
        self.json_file.close()

    def get_url(self):
        url = self.data["url"]
        return url

    def get_browser(self):
        browser = self.data["browser"]
        return browser

    def get_example_key_1(self):
        example_key_1 = self.data["example_key_1"]
        return example_key_1

    def get_example_key_2(self):
        example_key_2 = self.data["example_key_2"]
        return example_key_2

    def get_example_key_3(self):
        example_key_3 = self.data["example_key_3"]
        return example_key_3

    def get_alternate_value(self):
        alternate_value = self.data["alternate_value"]
        return alternate_value
