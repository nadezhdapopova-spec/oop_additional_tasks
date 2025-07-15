"""
Напишите класс Logger, имеющий следующие методы:

- __init__(self, filename): конструктор, принимающий имя файла, в который будет производиться запись логов;
- __call__(self, message): магический метод, который позволяет использовать объект класса Logger как функцию,
принимающую сообщение и записывающую его в файл.
"""


class Logger:
    filename: str

    def __init__(self, filename: str, mode: str = "r"):
        self.filename = filename
        self.mode = mode

    def __call__(self, message: str):
        with open(self.filename, self.mode) as f:
            f.write(message)


# код для проверки 
logger = Logger("log.txt", "w")
logger("This is a test message.")
