from src.tasks import Task


class User:
    username: str
    email: str
    first_name: str
    last_name: str
    task_list: list
    users_count = 0
    all_tasks_count = 0

    def __init__(self, username, email, first_name, last_name, task_list=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.task_list = task_list if task_list else []
        User.users_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0


if __name__ == "__main__":
    task1 = Task("Cдать домашку", "Cдать домашку 14.1 по ООП")
    task2 = Task("Cдать домашку", "Cдать домашку 14.2 по ООП")
    task3 = Task("Cдать домашку", "Cдать домашку 15.1 по ООП")
    task4 = Task("Cдать домашку", "Cдать домашку 15.2 по ООП")

    user1 = User("I_Ivan",
                 "I_Ivan@mail.ru",
                 "Иван",
                 "Иванов",
                 [task1, task2, task3, task4])

    print(user1.username)
    print(user1.email)
    print(user1.first_name)
    print(user1.last_name)
    print(user1.task_list)

    print(user1.users_count)
    print(User.all_tasks_count)
