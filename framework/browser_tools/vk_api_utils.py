from enum import Enum
import requests
from requests.exceptions import HTTPError
from tools.logger import Logger


class Methods(Enum):
    wall_post = 'wall.post'


class VKApiUtils:
    def __init__(self, token):
        self.basic_url = 'https://api.vk.com/method/'
        self.param_divider = '?'
        self.access_token_and_version = '&access_token=' + str(token) + '&v=5.122'

    def create_post(self, message):
        params = 'message=' + message
        url = self.basic_url + Methods.wall_post.value + self.param_divider + params + self.access_token_and_version
        response = requests.post(url)
        if response.status_code == 200:
            Logger(__name__).write_info('text /' + message + '/ has been sent')
            Logger(__name__).write_info('correct request response, status code - ' + str(response.status_code))
            try:
                Logger(__name__).write_info(response.json())
                return response.json()
            except HTTPError:
                Logger(__name__).write_error('incorrect json response')
        elif response.status_code != 200:
            Logger(__name__).write_warning('incorrect request response, status code - ' + str(response.status_code))
            return response.json()

    def edit_post(self, post_id, message, fileid):
        pass

    def upload_wall_image(self, filename):
        pass
