import requests

from config import ENDPOINT


def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)


def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")


def new_task_payload():
    return {
        "content": "test_content",
        "user_id": "test_user_id",
        "is_done": False,
    }


def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

