"""
Допишите код под условия в цикле так, чтобы вывод был корректным
"""


class Animal:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print('Bark!')


class Cat(Animal):

    def speak(self):
        print('Meow!')



animals = [Dog('Dog1'), Dog('Dog2'), Cat('Cat1'), Dog('Dog3')]

for animal in animals:  # Должно выводиться Bark или Meow в зависимости от того какой класс
    animal.speak()
