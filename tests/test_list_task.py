
def test_list_task(tasks):
    number_of_tasks = 3
    payload = tasks.new_task_payload()
    for _ in range(number_of_tasks):
        create_task_response = tasks.create_task(payload)
        assert create_task_response.status_code == 200

    user_id = payload["user_id"]
    list_task_response = tasks.list_task(user_id)
    assert list_task_response.status_code == 200

    data = list_task_response.json()
    tasks = data["tasks"]
    assert len(tasks) == number_of_tasks
