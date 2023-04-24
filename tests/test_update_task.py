
def test_update_task(tasks):
    payload = tasks.new_task_payload()
    create_task_response = tasks.create_task(payload)
    assert create_task_response.status_code == 200

    task_id = create_task_response.json()["task"]["task_id"]
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "test_updated_content",
        "is_done": True,
    }
    update_task_response = tasks.update_task(new_payload)
    assert update_task_response.status_code == 200

    get_task_response = tasks.get_task(task_id)
    assert get_task_response.status_code == 200

    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]
