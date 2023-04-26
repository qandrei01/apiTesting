import socket
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
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', 0))
            port = s.getsockname()[1]
        report_url = f"http://{ip_address}:{port}/index.html"
        terminalreporter.write_sep("-", f"Allure report: {report_url}")
    except subprocess.CalledProcessError as e:
        print(f"Check your setup for Allure. There was an error while generating report: \n {e}")
