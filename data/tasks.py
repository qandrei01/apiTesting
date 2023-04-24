import uuid

import requests

from config import ENDPOINT


class Tasks:

    @staticmethod
    def get_task(task_id):
        get_task_request = requests.get(ENDPOINT + f"/get-task/{task_id}")
        return get_task_request

    @staticmethod
    def update_task(payload):
        update_task_request = requests.put(ENDPOINT + "/update-task", json=payload)
        return update_task_request

    @staticmethod
    def list_task(user_id):
        list_task_request = requests.get(ENDPOINT + f"/list-tasks/{user_id}")
        return list_task_request

    @staticmethod
    def delete_task(task_id):
        delete_task_request = requests.delete(ENDPOINT + f"/delete-task/{task_id}")
        return delete_task_request

    @staticmethod
    def create_task(payload):
        create_task_request = requests.put(ENDPOINT + "/create-task", json=payload)
        return create_task_request

    @staticmethod
    def new_task_payload():
        user_id = f"test_user_{uuid.uuid4().hex}"
        content = f"test_content_{uuid.uuid4().hex}"
        return {
            "content": content,
            "user_id": user_id,
            "is_done": False,
        }


class AssertUtil:
    @staticmethod
    def assert_response(payload, expected_response=""):
        response = requests.put(ENDPOINT + "/create-task", json=payload)
        if response.status_code != expected_response:
            print(f"Task failed with status code {response.status_code}.")
        assert response.status_code == expected_response
