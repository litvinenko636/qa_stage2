from tools.logger import Logger


class BrowserActions:
    def __init__(self, driver):
        self.driver = driver

    def url_open(self, url):
        Logger(__name__).write_info(url + " is opened")
        return self.driver.get(url)

    def driver_close(self):
        Logger(__name__).write_info("Driver closed")
        return self.driver.close()

    def page_refresh(self):
        Logger(__name__).write_info("Refresh page")
        return self.driver.refresh()