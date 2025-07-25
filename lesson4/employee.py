"""
Напишите класс Employee, представляющий сотрудника, имеющий следующие методы:

- __init__(self, name, salary): конструктор, принимающий имя сотрудника и его зарплату;
- get_salary(self): метод, который возвращает зарплату сотрудника.

Напишите класс Manager, наследующийся от класса Employee, представляющий менеджера, имеющий следующие методы:

- __init__(self, name, salary, bonus): конструктор, принимающий имя менеджера, его зарплату и бонус;
- get_salary(self): метод, который возвращает зарплату менеджера плюс его бонус.
"""


class Employee:
    name: str
    salary: int | float

    def __init__(self, name: str, salary: int | float) -> None:
        self.name = name
        self.salary = salary

    def get_salary(self) -> int | float:
        return self.salary


class Manager(Employee):
    bonus: int | float

    def __init__(self, name: str, salary: int | float, bonus: int | float) -> None:
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self) -> int | float:
        if isinstance(self.salary, int | float) and isinstance(self.bonus, int | float):
            return self.salary + self.bonus
        raise TypeError


# код для проверки 
employee = Employee("John", 5000)
print(employee.get_salary())  # 5000

manager = Manager("Jane", 10000, 5000)
print(manager.get_salary())  # 15000
