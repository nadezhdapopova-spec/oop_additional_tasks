import pytest

from src.tasks import Task
from src.user import User


@pytest.fixture
def first_user():
    return User(
        username="user",
        email="user@mail.ru",
        first_name="User",
        last_name="Userov",
        task_list=[Task("Cдать домашку", "Cдать домашку 14.1 по ООП"),
                    Task("Cдать домашку", "Cдать домашку 14.2 по ООП")]
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
