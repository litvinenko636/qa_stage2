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

    def get_post_example(self):
        post_example = self.data["post_example"]
        return post_example
