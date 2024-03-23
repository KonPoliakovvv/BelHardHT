'''
Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и
меняет атрибут имени у объекта. Создать один объект класса. Вывести имя.
Вызвать метод change_name. Вывести имя.
'''

class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f"{self.name} прыгает!")

    def run(self):
        print(f"{self.name} бежит!")

    def bark(self):
        print(f"{self.name} лает!")

    def change_name(self, new_name):
        self.name = new_name
        print(f"Имя собаки изменено на {self.name}")

# Создание объекта класса Dog
dog = Dog(height=50, weight=20, name="Пушок", age=3)

# Вывод имени до изменения
print(f"Имя собаки: {dog.name}")

# Вызов метода change_name для изменения имени
dog.change_name("Шарик")

# Вывод имени после изменения
print(f"Имя собаки: {dog.name}")
