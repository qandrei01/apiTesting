import uuid

import requests

from config import ENDPOINT


def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)


def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")


def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"
    return {
        "content": content,
        "user_id": user_id,
        "is_done": False,
    }


def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)


def list_task(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")


def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")


def get_assert_response(payload, expected_response):
    response = requests.put(ENDPOINT + "/create-task", json=payload)
    if response.status_code != expected_response:
        print(f"Task failed with status code {response.status_code}.")
    assert response.status_code == expected_response
