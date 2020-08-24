from framework.driver.meta_singleton import MetaClassSingleton
from framework.driver.webdriver_factory import WebDriverFactory
from tools.json_reader import JsonReader


class Driver(metaclass=MetaClassSingleton):

    connection = None

    def connect(self):
        config = JsonReader('config.json')
        if self.connection is None:
            self.connection = WebDriverFactory.get_webdriver(config.get_browser())
        return self.connection
