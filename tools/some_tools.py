import random
import string


def random_string(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))


def user_item_add(user, item):
    return str(user) + '_' + str(item)
