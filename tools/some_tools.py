import random
import string


def random_string(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))


def post_user_id(str1, str2):
    return str(str1) + '_' + str(str2)
