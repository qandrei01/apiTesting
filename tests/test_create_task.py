import requests


def test_can_create_task(base_url):
    payload = {
        "content": "test_content",
        "user_id": "test_user_id",
        "task_id": "test_task_id",
        "is_done": False,
    }

    response = requests.put(base_url + "/create-task", json=payload, timeout=3)
    assert response.status_code == 200
