from tests.conftest import second_user


def test_user_init(first_user, second_user):
    assert first_user.username == "user"
    assert first_user.email == "user@mail.ru"
    assert len(first_user.tasks_list) == 2

    assert first_user.users_count == 2
    assert second_user.users_count == 2

    assert first_user.all_tasks_count == 4
    assert second_user.all_tasks_count == 4
