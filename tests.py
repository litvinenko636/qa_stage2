import pytest
from framework.api_utils import APIUtils


@pytest.mark.usefixtures('config')
def test1(config):

    resp = APIUtils(config.get_url())
    assert resp.get_status_code() == 200

    resp.get_json()