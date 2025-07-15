def test_user_init(first_user, second_user):
    assert first_user.username == "user"
    assert first_user.email == "user@mail.ru"
    assert len(first_user.task_in_list) == 2

    assert first_user.users_count == 2
    assert second_user.users_count == 2

    assert first_user.all_tasks_count == 4
    assert second_user.all_tasks_count == 4


def test_user_task_list_property(first_user):
    assert first_user.task_list == ("Cдать домашку, Статус выполнения: Ожидает старта, Дата создания: 15.07.2025\n"
                                    "Cдать домашку, Статус выполнения: Ожидает старта, Дата создания: 15.07.2025\n")


def test_user_task_list_setter(first_user, task):
    assert len(first_user.task_in_list) == 2
    first_user.task_list = task
    assert len(first_user.task_in_list) == 3
