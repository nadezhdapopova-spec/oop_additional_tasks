"""
Напишите класс Car, представляющий автомобиль, имеющий следующие методы:

- __init__(self, make, model, year): конструктор, принимающий марку автомобиля, модель и год выпуска;
- get_make(self): метод, который возвращает марку автомобиля;
- get_model(self): метод, который возвращает модель автомобиля;
- get_year(self): метод, который возвращает год выпуска автомобиля.

Напишите класс ElectricCar, наследующийся от класса Car, представляющий электромобиль, имеющий следующие методы:

- __init__(self, make, model, year, battery_size): конструктор, принимающий марку электромобиля, модель, год выпуска и размер батареи;
- get_battery_size(self): метод, который возвращает размер батареи электромобиля.
"""


class Car:
    make: str
    model: str
    year: int

    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def get_make(self) -> str:
        return self.make

    def get_model(self) -> str:
        return self.model

    def get_year(self) -> int:
        return self.year


class ElectricCar(Car):
    battery_size: int

    def __init__(self, make: str, model: str, year: int, battery_size: int) -> None:
        super().__init__(make, model, year)

        self.battery_size = battery_size

    def get_battery_size(self) -> int:
        return self.battery_size


# код для проверки 
car = Car("Tesla", "Model S", 2022)
print(car.get_make())  # Tesla
print(car.get_model())  # Model S
print(car.get_year())  # 2022

electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
print(electric_car.get_make())  # Tesla
print(electric_car.get_model())  # Model S
print(electric_car.get_year())  # 2022
print(electric_car.get_battery_size())  # 100
