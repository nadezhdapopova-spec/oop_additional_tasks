import pytest

from src.task_iterator import TaskIterator
from src.tasks import Task
from src.user import User


@pytest.fixture
def first_user():
    return User(
        username="user",
        email="user@mail.ru",
        first_name="User",
        last_name="Userov",
        task_list=[Task("Cдать домашку", "Cдать домашку 14.1 по ООП", created_at="15.07.2025"),
                    Task("Cдать домашку", "Cдать домашку 14.2 по ООП", created_at="15.07.2025")]
    )


@pytest.fixture
def second_user():
    return User(
        username="user_2",
        email="user_2@mail.ru",
        first_name="User_2",
        last_name="Userov_2",
        task_list=[Task("Cдать домашку", "Cдать домашку 15.1 по ООП"),
                    Task("Cдать домашку", "Cдать домашку 15.2 по ООП")]
    )


@pytest.fixture
def task():
    return Task("Cдать домашку", "Cдать домашку 15.1 по ООП", created_at="20.06.2025")


@pytest.fixture
def task_with_runtime1():
    return Task("Cдать домашку1", "Cдать домашку 16.1 по ООП", created_at="20.06.2025", run_time=60)


@pytest.fixture
def task_with_runtime2():
    return Task("Cдать домашку2", "Cдать домашку 16.2 по ООП", created_at="20.06.2025", run_time=30)


@pytest.fixture
def task_iterator(second_user):
    return TaskIterator(second_user)
