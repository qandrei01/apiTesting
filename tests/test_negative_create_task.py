import requests


def test_create_without_content(base_url):
    payload = {
        "user_id": "test_user_id",
        "task_id": "test_task_id",
        "is_done": False,
    }

    response = requests.put(base_url + "/create-task", json=payload)
    if response.status_code != 200:
        print(f"Task failed with status code {response.status_code}.")
    else:
        print(f"Task passed unexpectedly with status code {response.status_code}.")
    assert response.status_code != 200


def test_create_without_user(base_url):
    payload = {
        "content": "test_content",
        "task_id": "test_task_id",
        "is_done": False,
    }

    response = requests.put(base_url + "/create-task", json=payload)
    if response.status_code != 200:
        print(f"Task failed with status code {response.status_code}.")
    else:
        print(f"Task passed unexpectedly with status code {response.status_code}.")
    assert response.status_code != 200


def test_create_without_task(base_url):
    payload = {
        "content": "test_content",
        "user_id": "test_user_id",
        "is_done": False,
    }

    response = requests.put(base_url + "/create-task", json=payload)
    if response.status_code != 200:
        print(f"Task failed with status code {response.status_code}.")
    else:
        print(f"Task passed unexpectedly with status code {response.status_code}.")
    assert response.status_code != 200


def test_create_without_done(base_url):
    payload = {
        "content": "test_content",
        "user_id": "test_user_id",
        "task_id": "test_task_id",
    }

    response = requests.put(base_url + "/create-task", json=payload)
    if response.status_code != 200:
        print(f"Task failed with status code {response.status_code}.")
    else:
        print(f"Task passed unexpectedly with status code {response.status_code}.")
    assert response.status_code != 200


def test_create_empty(base_url):
    payload = {
    }

    response = requests.put(base_url + "/create-task", json=payload)
    if response.status_code != 200:
        print(f"Task failed with status code {response.status_code}.")
    else:
        print(f"Task passed unexpectedly with status code {response.status_code}.")
    assert response.status_code != 200


def test_create_with_wrong_data(base_url):
    payload = {
        "test1": "test_content",
        "test2": "test_user_id",
        "test3": "test_task_id",
        "test4": False,
    }

    response = requests.put(base_url + "/create-task", json=payload)
    if response.status_code != 200:
        print(f"Task failed with status code {response.status_code}.")
    else:
        print(f"Task passed unexpectedly with status code {response.status_code}.")
    assert response.status_code != 200


def test_create_with_extra_data(base_url):
    payload = {
        "content": "test_content",
        "user_id": "test_user_id",
        "task_id": "test_task_id",
        "is_done": False,
        "extra_data": "test"
    }

    response = requests.put(base_url + "/create-task", json=payload)
    if response.status_code != 200:
        print(f"Task failed with status code {response.status_code}.")
    else:
        print(f"Task passed unexpectedly with status code {response.status_code}.")
    assert response.status_code != 200
