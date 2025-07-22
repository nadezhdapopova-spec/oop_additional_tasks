"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""
from datetime import datetime


class Car:
    brand: str
    model: str
    age: int

    def __init__(self, brand: str, model: str, age: int) -> None:
        self.brand = brand
        self.model = model
        self.age = self.validate_age(age)

    @staticmethod
    def validate_age(age: int) -> int:
        if age > datetime.now().year:
            raise ValueError("Эта машина еще не была выпущена")
        return age


# код для проверки
car = Car('Toyota', 'Corolla', 2022)

print(car.brand)
print(car.model)
print(car.age)

car = Car('Toyota', 'Corolla', 3000)
# raises Exception('Эта машина еще не была выпущена')
print(car.brand)
print(car.model)
print(car.age)
