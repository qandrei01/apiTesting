import requests

from data.get_url import ENDPOINT


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
