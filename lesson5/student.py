"""
Напишите класс Student, представляющий студента, имеющий следующие атрибуты:

- __slots__ = ('name', 'age', 'grades'): список атрибутов, доступных объекту.

Напишите класс Course, представляющий курс, имеющий следующие атрибуты:

- __slots__ = ('name', 'students'): список атрибутов, доступных объекту.
"""


class Student:
    __slots__ = ("name", "age", "grades")


class Course:
    __slots__ = ("name", "students")


# код для проверки 
student1 = Student()
student1.name = "John"
student1.age = 20
student1.grades = [90, 80, 85]

student2 = Student()
student2.name = "Jane"
student2.age = 21
student2.grades = [95, 85, 90]

course = Course()
course.name = "Math"
course.students = [student1, student2]

print(student1.name)
print(student1.age)
print(student1.grades)

print(student2.name)
print(student2.age)
print(student2.grades)

print(course.name)
print(course.students[0].name)
print(course.students[1].grades)
