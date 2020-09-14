import pytest
from framework.api_utils import APIUtils


@pytest.mark.usefixtures('config')
def test1(config):
    resp = APIUtils(config.get_url())

    assert resp.get_status_code() == 200
    assert resp.get_items('posts') == 200
    assert resp.get_item('posts', 99) == 200
    assert resp.get_item('posts', 150) == 404
    assert resp.post_item('posts', json=config.get_post_example()) == 201
    assert resp.get_items('users') == 200
    assert resp.get_item('users', 5) == 200
