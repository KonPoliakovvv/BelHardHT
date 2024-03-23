'''
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на
экран. Создать объект класса Dog, вызвать все методы объекта и вывести на
экран все его атрибуты.
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

# Создание объекта класса Dog
dog = Dog(height=50, weight=20, name="Пушок", age=3)

# Вызов методов объекта
dog.jump()
dog.run()
dog.bark()

# Вывод всех атрибутов объекта
print(f"Имя: {dog.name}")
print(f"Возраст: {dog.age}")
print(f"Рост: {dog.height}")
print(f"Вес: {dog.weight}")
