from enum import Enum
import requests
from requests.exceptions import HTTPError
from tools.logger import Logger
from tools.some_tools import user_post_add


class Methods(Enum):
    wall_post_create = 'wall.post'
    wall_post_edit = 'wall.edit'
    wall_upload_server = 'photos.getWallUploadServer'
    wall_post_delete = 'wall.delete'
    wall_comment_create = 'wall.createComment'
    photos_save = 'photos.saveWallPhoto'


class VKApiUtils:
    def __init__(self, token):
        self.basic_url = 'https://api.vk.com/method/'
        self.param_divider = '&'
        self.method_divider = '?'
        self.access_token_and_version = '&access_token=' + str(token) + '&v=5.122'

    def create_post(self, message):
        params = 'message=' + message
        url = self.basic_url + Methods.wall_post_create.value + self.method_divider + params + self.access_token_and_version
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

    def edit_post(self, photo_info, message, post_id):
        photo_id = str(photo_info['response'][0]['id'])
        photo = 'photo' + str(photo_info['response'][0]['owner_id']) + '_' + photo_id
        params = 'message=' + message + self.param_divider + 'attachments=' + photo + self.param_divider + 'post_id=' + str(post_id)
        Logger(__name__).write_info('text /' + message + '/ has been sent')
        url = self.basic_url + Methods.wall_post_edit.value + self.method_divider + params + self.access_token_and_version
        requests.post(url)

    def upload_wall_image(self):
        server_info = VKApiUtils.get_server_address(self)
        upload_url = server_info['response']['upload_url']
        photo = {'photo': open('image.jpg', 'rb')}
        response = requests.post(upload_url, files=photo)
        return response.json()

    def save_wall_image(self):
        response = VKApiUtils.upload_wall_image(self)
        params = 'server=' + str(response['server']) + self.param_divider + 'photo=' + response['photo'] + self.param_divider + 'hash=' + response['hash']
        url = self.basic_url + Methods.photos_save.value + self.method_divider + params + self.access_token_and_version
        result = requests.post(url)
        return result.json()

    def get_server_address(self):
        params = ''
        url = self.basic_url + Methods.wall_upload_server.value + self.method_divider + params + self.access_token_and_version
        response = requests.get(url)
        return response.json()

    def create_comment(self, post_id, message):
        params = 'post_id=' + str(post_id) + self.param_divider + 'message=' + message
        url = self.basic_url + Methods.wall_comment_create.value + self.method_divider + params + self.access_token_and_version
        response = requests.get(url)
        Logger(__name__).write_info('text /' + message + '/ has been sent')
        Logger(__name__).write_info(response.json())
        return response.json()

    def delete_post(self, post_id):
        params = 'post_id=' + str(post_id)
        url = self.basic_url + Methods.wall_post_delete.value + self.method_divider + params + self.access_token_and_version
        response = requests.post(url)
        Logger(__name__).write_info(response.json())
        if response.json()['response'] == 1:
            Logger(__name__).write_info('successful post deleting')
        return response.json()