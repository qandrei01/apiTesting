import requests


def test_get_task_id(base_url):
    payload = {
        "content": "test_content",
        "user_id": "test_user_id",
        "is_done": False,
    }
    create_task_response = requests.put(base_url + "/create-task", json=payload, timeout=2)
    assert create_task_response.status_code == 200

    data = create_task_response.json()
    task_id = data["task"]["task_id"]
    get_task_response = requests.get(base_url + f"/get-task/{task_id}", timeout=2)
    assert get_task_response.status_code == 200

    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]
