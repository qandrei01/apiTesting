
from datetime import datetime, timedelta

import requests


def test_can_call_endpoint(base_url):
    response = requests.get(base_url, timeout=2)
    assert response.status_code == 200

    get_response_date = response.headers.get("Date")
    format_response_date_dt = datetime.strptime(get_response_date, "%a, %d %b %Y %H:%M:%S %Z")
    response_date = format_response_date_dt.isoformat()
    actual_date = datetime.utcnow().isoformat()
    actual_date_dt = datetime.fromisoformat(actual_date)
    response_date_dt = datetime.fromisoformat(response_date)
    time_diff = abs(actual_date_dt - response_date_dt)
    assert time_diff <= timedelta(seconds=1)
