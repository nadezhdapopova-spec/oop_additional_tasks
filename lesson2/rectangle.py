"""
Напишите класс Rectangle, имеющий следующие методы:

- __init__(self, width, height): конструктор, принимающий ширину и высоту прямоугольника
- area(self): метод, возвращающий площадь прямоугольника
- perimeter(self): метод, возвращающий периметр прямоугольника
- from_diagonal(cls, diagonal, aspect_ratio): класс-метод, принимающий диагональ прямоугольника и соотношение сторон и возвращающий объект класса Rectangle
- is_square(width, height): статический метод, принимающий ширину и высоту прямоугольника и возвращающий True,
если это квадрат, и False в противном случае
"""
from math import sqrt


class Rectangle:
    width: float
    height: float

    def __init__(self, width, height):
        self._width = width
        self._height = height


    def area(self):
        return self._width * self._height


    def perimeter(self):
        return (self._width + self._height) * 2


    @classmethod
    def from_diagonal(cls, diagonal, aspect_ratio):
        width = diagonal / sqrt(aspect_ratio ** 2 + 1)
        height = width * 2
        return cls(width, height)


    @staticmethod
    def is_square(width, height):
        return width == height


# код для проверки 
rectangle = Rectangle(4, 5)
print(rectangle.area())  # 20
print(rectangle.perimeter())  # 18

rectangle2 = Rectangle.from_diagonal(5, 2)
print(rectangle2.area())  # 10.0128
print(rectangle2.perimeter())  # 13.42

print(Rectangle.is_square(4, 4))  # True
print(Rectangle.is_square(4, 5))  # False
