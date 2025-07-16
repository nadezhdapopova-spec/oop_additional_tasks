from datetime import datetime

from src.tasks import Task


def test_tasks_init(task):
    assert task.name == "Cдать домашку"
    assert task.description == "Cдать домашку 15.1 по ООП"
    assert task.status == "Ожидает старта"
    assert task.created_at == "20.06.2025"


def test_task_list_create():
    """Проверка создания новой задачи"""
    task = Task("Купить билеты", "Купить билеты на самолет")
    task.name = "Купить билеты"
    task.description = "Купить билеты на самолет"
    task.status = "Ожидает старта"
    task.created_at = datetime.now().date().strftime("%d.%m.%Y")


def test_task_update(capsys, task):
    task.created_at = "10.07.2025"
    message = capsys.readouterr()
    assert message.out.strip() == "Нельзя изменить дату создания на дату из прошлого"

    task.created_at = datetime.now().date().strftime("%d.%m.%Y")
    assert task.created_at == datetime.now().date().strftime("%d.%m.%Y")


def test_task_str(task):
    assert str(task) == "Cдать домашку, Статус выполнения: Ожидает старта, Дата создания: 20.06.2025"


def test_task_add(task_with_runtime1, task_with_runtime2):
    assert task_with_runtime1 + task_with_runtime2 == 90
