from datetime import datetime

class Task:
    name: str
    description: str
    status: str
    created_at: str

    def __init__(self, name, description, status="Ожидает старта", created_at=None):
        self.name = name
        self.description = description
        self.status = status
        self.__created_at = created_at if created_at else datetime.today().strftime("%d.%m.%Y")

    def __str__(self):
        return f"{self.name}, Статус выполнения: {self.status}, Дата создания: {self.created_at}"

    @classmethod
    def new_task(cls, name, description, status="Ожидает старта", created_at=None):
        return cls(name, description, status, created_at)

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, new_date: str):
        if datetime.strptime(new_date, "%d.%m.%Y").date() < datetime.now().date():
            print("Нельзя изменить дату создания на дату из прошлого")
            return
        self.__created_at = new_date

if __name__ == "__main__":
    task1 = Task("Cдать домашку", "Cдать домашку по ООП")

    print(task1.name)
    print(task1.description)
    print(task1.status)
    print(task1.created_at)

    task2 = Task("Купить билеты", "Купить билеты на самолет")

    print(task2.name)
    print(task2.description)
    print(task2.status)
    print(task2.created_at)

    task2.created_at = "10.07.2025"
    print(task2.created_at)
    task2.created_at = "10.08.2025"
    print(task2.created_at)
