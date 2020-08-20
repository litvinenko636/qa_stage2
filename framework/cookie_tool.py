class CookieTool:
    def __init__(self, driver):
        self.driver = driver

    def add_cookie(self, cookie_name, cookie_value):
        return self.driver.add_cookie({"name": cookie_name, "value": cookie_value})

    def delete_all_cookies(self):
        return self.driver.delete_all_cookies()

    def delete_cookie(self, cookie_name):
        return self.driver.delete_cookie(cookie_name)
