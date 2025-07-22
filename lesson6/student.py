"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число
- Оценки - список из целых чисел, может быть пустым

Опишите класс Student и метод avg_rate так, чтобы считалась средняя оценка, а при пустом списке оценок возвращался 0

"""


class Student:
    name: str
    course: int
    grades: list[int] | list[None]

    def __init__(self, name: str, course: int, grades: list[int] | list[None]):
        self.name = name
        self.course = course
        self.grades = grades

    def avg_rate(self):
        print(round(sum(self.grades) / len(self.grades), 2) if len(self.grades) > 0 else 0)


# код для проверки
student = Student('Ivan', 'Python', [5, 4, 5, 5])
student.avg_rate() # 4.75

student = Student('Ivan', 'Python', [])
student.avg_rate() # 0.0
