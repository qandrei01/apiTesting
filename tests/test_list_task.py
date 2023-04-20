from data.tasks import new_task_payload, create_task, list_task


def test_list_task():
    tasks_number = 3
    payload = new_task_payload()
    for _ in range(tasks_number):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    user_id = payload["user_id"]
    list_task_response = list_task(user_id)
    assert list_task_response.status_code == 200

    data = list_task_response.json()
    tasks = data["tasks"]
    assert len(tasks) == tasks_number
