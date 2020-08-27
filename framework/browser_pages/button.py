import os
import time
import pyautogui
from framework.browser_pages.base_element import BaseElement
from tools.logger import Logger


class Button(BaseElement):
    # тут могут находится методы по получению атрибутов(?)

    @staticmethod
    def file_upload(filepath):
        try:
            time.sleep(3)
            pyautogui.write(os.path.abspath(os.getcwd() + filepath))  # path of File
            pyautogui.press('enter')
            Logger(__name__).write_info(filepath + ' - has been sent')
            return True
        except:
            Logger(__name__).write_error('incorrect uploading!')
            return False