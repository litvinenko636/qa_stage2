import pytest
from framework.api_utils import APIUtils


@pytest.mark.usefixtures('config')
def test1(config):
    resp = APIUtils(config.get_url())

    assert resp.get_status_code() == 200
    assert resp.get_items('posts')[0] == 200
    assert resp.get_item('posts', 99)[0] == 200
