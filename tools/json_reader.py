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

    def get_email(self):
        email = self.data["email"]
        return email

    def get_password(self):
        password = self.data["password"]
        return password

    def get_token(self):
        token = self.data["token"]
        return token

    def get_user_id(self):
        user_id = self.data["user_id"]
        return user_id
