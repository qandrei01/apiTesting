import requests


def test_can_call_endpoint(base_url):
    response = requests.get(base_url, timeout=2)
    assert response.status_code == 200
