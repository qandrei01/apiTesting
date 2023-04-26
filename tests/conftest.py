import os
import subprocess

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


@pytest.hookimpl(trylast=True)
def pytest_terminal_summary(terminalreporter):
    try:
        generate_report = subprocess.run(("allure", "generate", "-c"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        generate_report.check_returncode()
        terminalreporter.write_sep("-", f"Allure report: http://{os.path.abspath('index.html')})")
    except subprocess.CalledProcessError as e:
        print(f"Check your setup for Allure. There was an error while generating report: \n {e}")
