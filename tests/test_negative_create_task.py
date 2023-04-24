

def test_create_without_content(base_url, assert_util):
    payload = {
        "user_id": "test_user_id",
        "task_id": "test_task_id",
        "is_done": False,
    }
    assert_util.assert_response(payload, expected_response=422)


def test_create_without_user(base_url, assert_util):
    payload = {
        "content": "test_content",
        "task_id": "test_task_id",
        "is_done": False,
    }

    assert_util.assert_response(payload, expected_response=500)


def test_create_without_task(base_url, assert_util):
    payload = {
        "content": "test_content",
        "user_id": "test_user_id",
        "is_done": False,
    }

    assert_util.assert_response(payload, expected_response=200)


def test_create_without_done(base_url, assert_util):
    payload = {
        "content": "test_content",
        "user_id": "test_user_id",
        "task_id": "test_task_id",
    }

    assert_util.assert_response(payload, expected_response=200)


def test_create_with_done_True(base_url, assert_util):
    payload = {
        "content": "test_content",
        "user_id": "test_user_id",
        "task_id": "test_task_id",
        "is_done": True,
    }

    assert_util.assert_response(payload, expected_response=200)


def test_create_empty(base_url, assert_util):
    payload = {
    }

    assert_util.assert_response(payload, expected_response=422)


def test_create_with_wrong_data(base_url, assert_util):
    payload = {
        "test1": "test_content",
        "test2": "test_user_id",
        "test3": "test_task_id",
        "test4": False,
    }

    assert_util.assert_response(payload, expected_response=422)


def test_create_with_extra_data(base_url, assert_util):
    payload = {
        "content": "test_content",
        "user_id": "test_user_id",
        "task_id": "test_task_id",
        "is_done": False,
        "extra_data": "test"
    }

    assert_util.assert_response(payload, expected_response=200)
