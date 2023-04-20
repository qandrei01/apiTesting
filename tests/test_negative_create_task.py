from data import tasks


def test_create_without_content(base_url):
    payload = {
        "user_id": "test_user_id",
        "task_id": "test_task_id",
        "is_done": False,
    }
    tasks.get_assert_response(payload, expected_response=422)


def test_create_without_user(base_url):
    payload = {
        "content": "test_content",
        "task_id": "test_task_id",
        "is_done": False,
    }

    tasks.get_assert_response(payload, expected_response=500)


def test_create_without_task(base_url):
    payload = {
        "content": "test_content",
        "user_id": "test_user_id",
        "is_done": False,
    }

    tasks.get_assert_response(payload, expected_response=200)


def test_create_without_done(base_url):
    payload = {
        "content": "test_content",
        "user_id": "test_user_id",
        "task_id": "test_task_id",
    }

    tasks.get_assert_response(payload, expected_response=200)


def test_create_with_done_True(base_url):
    payload = {
        "content": "test_content",
        "user_id": "test_user_id",
        "task_id": "test_task_id",
        "is_done": True,
    }

    tasks.get_assert_response(payload, expected_response=200)


def test_create_empty(base_url):
    payload = {
    }

    tasks.get_assert_response(payload, expected_response=422)


def test_create_with_wrong_data(base_url):
    payload = {
        "test1": "test_content",
        "test2": "test_user_id",
        "test3": "test_task_id",
        "test4": False,
    }

    tasks.get_assert_response(payload, expected_response=422)


def test_create_with_extra_data(base_url):
    payload = {
        "content": "test_content",
        "user_id": "test_user_id",
        "task_id": "test_task_id",
        "is_done": False,
        "extra_data": "test"
    }

    tasks.get_assert_response(payload, expected_response=200)
