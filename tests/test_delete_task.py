
def test_delete_task(tasks):

    payload = tasks.new_task_payload()
    create_task_response = tasks.create_task(payload)
    assert create_task_response.status_code == 200

    task_id = create_task_response.json()["task"]["task_id"]
    delete_task_response = tasks.delete_task(task_id)
    assert delete_task_response.status_code == 200

    get_task_response = tasks.get_task(task_id)
    assert get_task_response.status_code == 404
