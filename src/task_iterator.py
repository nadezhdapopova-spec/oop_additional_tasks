from src.tasks import Task
from src.user import User


class TaskIterator:
    user_obj: User

    def __init__(self, user_obj: User):
        self.user = user_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.user.task_in_list):
            task = self.user.task_in_list[self.index]
            self.index += 1
            return task
        else:
            raise StopIteration


if __name__ == "__main__":
    task1 = Task("Cдать домашку 1", "Cдать домашку 14.1 по ООП")
    task2 = Task("Cдать домашку 2", "Cдать домашку 14.2 по ООП")
    task3 = Task("Cдать домашку 3", "Cдать домашку 15.1 по ООП")
    task4 = Task("Cдать домашку 4", "Cдать домашку 15.2 по ООП")

    user1 = User("I_Ivan",
                 "I_Ivan@mail.ru",
                 "Иван",
                 "Иванов",
                 [task1, task2, task3, task4])

    iterator = TaskIterator(user1)

    for task in iterator:
        print(task)
    print()

    for task in iterator:
        print(task)
