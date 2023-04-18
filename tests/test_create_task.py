import requests

from data.get_url import ENDPOINT


def test_can_create_task():
    payload = {
        "content": "test_content",
        "user_id": "test_user_id",
        "task_id": "test_task_id",
        "is_done": False,
    }

    response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert response.status_code == 200
