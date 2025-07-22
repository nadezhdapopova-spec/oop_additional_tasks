from src.tasks import Task


class DeadlineTask(Task):
    deadline: str

    def __init__(self, name, description, deadline, status="Ожидает старта", created_at=None, run_time=0):
        super().__init__(name, description, status, created_at, run_time)
        self.deadline = deadline

    def __add__(self, other):
        if type(other) is DeadlineTask:
            return self.run_time + other.run_time
        raise TypeError


if __name__ == "__main__":
    deadline_task = DeadlineTask("Купить учебник",
                                 "Купить учебник по программированию",
                                 "30.07.2025",
                                 run_time=60)
    print(deadline_task.name)
    print(deadline_task.description)
    print(deadline_task.status)
    print(deadline_task.created_at)
    print(deadline_task.run_time)

    print(deadline_task.deadline)

    deadline_task_2 = DeadlineTask("Купить учебник",
                                 "Купить учебник по ООП",
                                 "30.07.2025",
                                 run_time=120)

    task = Task("Cдать домашку", "Cдать домашку по ООП", run_time=120)

    print(deadline_task + deadline_task_2)
    # print(deadline_task + task)
