from framework.driver.webdriver_singleton import Driver


class IFrameTool:
    def __init__(self, frame_reference):
        self.driver = Driver().connect()
        self.frame = frame_reference

    def iframe_open(self):
        return self.driver.switch_to.frame(self.frame)

    def iframe_close(self):
        return self.driver.switch_to.default_content()