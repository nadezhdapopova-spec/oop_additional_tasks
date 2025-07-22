"""
Для класса Employee и Client, опишите магический метод сложения таким образом, чтобы результатом сложения
было число, а прибавлять можно было только числа или другие объекты дочерних классов Employee

"""
from typing import Any


class Employee:
    pay: int | float

    def __init__(self, pay: int | float) -> None:
        self.pay = pay

    def __add__(self, other: Any) -> int | float:
        if isinstance(other, (int, float)):
            return self.pay + other
        if issubclass(other, Employee):
            return self.pay + other.pay
        raise TypeError


class Client:
    pay: int | float

    def __init__(self, pay: int | float) -> None:
        self.pay = pay

    def __add__(self, other: Any) -> int | float:
        if isinstance(other, (int, float)):
            return self.pay + other
        if isinstance(other, Client):
            pass
        raise TypeError


class Developer(Employee):
    pass


class Manager(Employee):
    pass


# код для проверки
users = [Employee(50000), Client(100000), Developer(50000), Manager(50000)]

total_salary = 0
for user in users:
    if isinstance(user, Employee):
        total_salary = user + total_salary

print(total_salary)
# Вывод: 150000
