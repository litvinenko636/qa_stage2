from framework.driver.webdriver_singleton import Driver
from tools.logger import Logger


class BrowserActions:
    def __init__(self):
        self.driver = Driver().connect()

    def url_open(self, url):
        Logger(__name__).write_info(url + " is opened")
        return self.driver.get(url)

    def driver_close(self):
        Logger(__name__).write_info("driver closed")
        return self.driver.close()

    def page_refresh(self):
        Logger(__name__).write_info("refresh page")
        return self.driver.refresh()