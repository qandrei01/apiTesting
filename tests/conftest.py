import pytest

from config import ENDPOINT


@pytest.fixture(scope='session')
def base_url():
    return ENDPOINT
