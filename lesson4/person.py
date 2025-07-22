"""
Напишите класс Person, представляющий человека, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя человека и его возраст;
- get_name(self): метод, который возвращает имя человека;
- get_age(self): метод, который возвращает возраст человека.

Напишите класс Student, наследующийся от класса Person, представляющий студента, имеющий следующие методы:

- __init__(self, name, age, major): конструктор, принимающий имя студента, его возраст и основной предмет
- get_major(self): метод, который возвращает основной предмет студента.
"""


class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age


class Student(Person):
    major: str

    def __init__(self, name: str, age: int, major: str) -> None:
        super().__init__(name, age)

        self.major = major

    def get_major(self) -> str:
        return self.major


# код для проверки 
person = Person("Иван", 25)
print(person.get_name())  # Иван
print(person.get_age())  # 25

student = Student("Мария", 20, "математика")
print(student.get_name())  # Мария
print(student.get_age())  # 20
print(student.get_major())  # математика
