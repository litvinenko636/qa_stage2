class BrowserActions:
    def __init__(self, driver):
        self.driver = driver

    def url_open(self, url):
        return self.driver.get(url)

    def driver_close(self):
        return self.driver.close()

    def page_refresh(self):
        return self.driver.refresh()