from tools.logger import Logger


class CookieTool:
    def __init__(self, driver):
        self.driver = driver

    def add_some_cookie(self, cookie_name, cookie_value):
        cookie_dict = {"name": cookie_name, "value": cookie_value}
        cookie_add = self.driver.add_cookie(cookie_dict)
        Logger(__name__).write_info('Cookie ' + str(cookie_dict) + ' is added!')
        try:
            cookie_added = self.get_some_cookie(cookie_name)
            assert {cookie_added['name']: cookie_added['value']} == {cookie_name: cookie_value}
            Logger(__name__).write_info('assertion is correct!')
        except AssertionError:
            Logger(__name__).write_error('assertion error!')
        finally:
            return cookie_add

    def get_some_cookie(self, cookie_name):
        return self.driver.get_cookie(cookie_name)

    def get_all_cookies(self):
        return self.driver.get_cookies()

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()
        Logger(__name__).write_info('cookies is deleted!')
        try:
            assert self.get_all_cookies() == []
            Logger(__name__).write_info('assertion is correct!')
        except AssertionError:
            Logger(__name__).write_error('assertion error!')
            return False
        finally:
            return True

    def delete_cookie(self, cookie_name):
        self.driver.delete_cookie(cookie_name)
        Logger(__name__).write_info('Cookie ' + cookie_name + ' is deleted!')
        try:
            assert self.get_some_cookie(cookie_name) is None
            Logger(__name__).write_info('Assertion is correct!')
        except AssertionError:
            Logger(__name__).write_error('Assertion error!')
            return False
        finally:
            return True
