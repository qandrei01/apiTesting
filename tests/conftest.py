import pytest

from config import ENDPOINT
from data.tasks import Tasks, AssertUtil


@pytest.fixture(scope='session')
def base_url():
    return ENDPOINT


@pytest.fixture()
def tasks():
    tasks = Tasks
    return tasks


@pytest.fixture()
def assert_util():
    assert_util = AssertUtil
    return assert_util
