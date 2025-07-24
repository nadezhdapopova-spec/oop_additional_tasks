"""
Напишите класс Shape, представляющий геометрическую фигуру, имеющий следующие методы:

- __init__(self, name): конструктор, принимающий имя геометрической фигуры;
- area(self): метод, который вычисляет площадь геометрической фигуры.

Напишите класс Rectangle, наследующийся от класса Shape, представляющий прямоугольник, имеющий следующие методы:

- __init__(self, name, width, height): конструктор, принимающий имя прямоугольника, ширину и высоту;
- area(self): метод, который вычисляет площадь прямоугольника.

Напишите класс Triangle, наследующийся от класса Shape, представляющий треугольник, имеющий следующие методы:

- __init__(self, name, base, height): конструктор, принимающий имя треугольника, основание и высоту;
- area(self): метод, который вычисляет площадь треугольника.
"""


class Shape:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def area(self) -> int:
        return 0


class Rectangle(Shape):
    width: int | float
    height: int | float

    def __init__(self, name: str, width: int | float, height: int | float) -> None:
        super().__init__(name)

        self.height = height
        self.width = width

    def area(self) -> int | float:
        return self.height * self.width


class Triangle(Shape):
    base: int | float
    height: int | float

    def __init__(self, name: str, base: int | float, height: int | float) -> None:
        super().__init__(name)

        self.height = height
        self.base = base

    def area(self) -> int | float:
        return (self.height * self.base) / 2


# код для проверки 
shape = Shape("Shape")
print(shape.area())  # 0

rect = Rectangle("Rectangle", 5, 10)
print(rect.area())  # 50

tri = Triangle("Triangle", 6, 4)
print(tri.area())  # 12
