from src.tasks import Task


class PeriodicTask(Task):
    start_date: str
    end_date: str
    frequency: str

    def __init__(self,
                 name,
                 description,
                 start_date,
                 end_date,
                 status="Ожидает старта",
                 created_at=None,
                 run_time=0,
                 frequency="Ежедневная"):
        super().__init__(name, description, status, created_at, run_time)
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency

    def __add__(self, other):
        if type(other) is PeriodicTask:
            return self.run_time + other.run_time
        raise TypeError


if __name__ == "__main__":
    periodic_task = PeriodicTask("Купить книгу",
                                 "Купить книгу по кулинарии",
                                 "23.07.2025",
                                 "23.07.2025",
                                 run_time=60)
    print(periodic_task.name)
    print(periodic_task.description)
    print(periodic_task.status)
    print(periodic_task.created_at)

    print(periodic_task.start_date)
    print(periodic_task.end_date)
    print(periodic_task.frequency)

    periodic_task_2 = PeriodicTask("Купить книгу",
                                 "Купить книгу по медитации",
                                 "23.07.2025",
                                 "23.07.2025",
                                 run_time=60)

    task = Task("Cдать домашку", "Cдать домашку по ООП", run_time=60)

    print(periodic_task + periodic_task_2)
    # print(periodic_task + task)
