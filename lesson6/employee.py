"""
Напишите класс Person, представляющий человека, имеющий следующие атрибуты:

- имя
- возраст
- зарплата

Напишите класс Employee, у которого конструктор проверяет, что возраст не меньше 18 и не больше 127 лет.
В случае, если возраст не укладывается в заданные рамки, вызвать исключение ValueError и прервать выполнение программы.
Также в конструкторе необходимо проверять уровень зарплаты, который должен быть не меньше 16242. Вызывать ValueError
исключение.

Вызванные исключения должны пояснять в чем именно произошла ошибка.
"""

class Person:
    name: str
    age: int
    salary: int | float

    def __init__(self, name: str, age: int, salary: int | float) -> None:
        self.name = name
        self.age = age
        self.salary = salary


class Employee:
    name: str
    age: int
    salary: int | float

    def __init__(self, name: str, age: int, salary: int | float) -> None:
        self.name = name
        self.age = self.validate_age(age)
        self.salary = self.validate_salary(salary)

    @staticmethod
    def validate_age(age):
        if 18 <= age <= 127:
            return age
        raise ValueError("Возраст должен быть не меньше 18 и не больше 127")

    @staticmethod
    def validate_salary(salary):
        if salary >= 16242:
            return salary
        raise ValueError("Оплата труда не может быть меньше 16242")


# код для проверки
employee = Employee('John', 30, 5000)
# raises ValueError('Оплата труда не может быть меньше 16242')

employee = Employee("Jane", 17, 50000)
# raises ValueError('Возраст должен быть не меньше 18 и не больше 127')

employee = Employee("Kate", 175, 50000)
# raises ValueError('Возраст должен быть не меньше 18 и не больше 127')
