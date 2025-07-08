def test_tasks_init(task):
    assert task.name == "Cдать домашку"
    assert task.description == "Cдать домашку 15.1 по ООП"
    assert task.status == "Ожидает старта"
    assert task.created_at == "20.06.2025"
