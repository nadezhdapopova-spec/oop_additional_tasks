def test_print_mixin_task(capsys, task):
    message = capsys.readouterr()
    assert message.out.strip() == "Task(Cдать домашку, Cдать домашку 15.1 по ООП, Ожидает старта, 20.06.2025)"


def test_print_mixin_periodic_task(capsys, task_periodic_1):
    message = capsys.readouterr()
    assert message.out.strip() == "PeriodicTask(Купить книгу, Купить книгу по кулинарии, Ожидает старта, 24.07.2025)"


def test_print_mixin_deadline_task(capsys, task_deadline_1):
    message = capsys.readouterr()
    assert (message.out.strip() ==
            "DeadlineTask(Купить учебник, Купить учебник по программированию, Ожидает старта, 24.07.2025)")
