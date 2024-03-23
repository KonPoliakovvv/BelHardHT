'''
Task_4_2
Собрать с помощью декораторов чикенбургер:
- булка
- сыр
- салат
- курица
- булка
'''


def bun(func):
    def wrapper():
        print("Булка")
        func()
        print("Булка")
    return wrapper

def cheese(func):
    def wrapper():
        print("Сыр")
        func()
    return wrapper

def salad(func):
    def wrapper():
        print("Салат")
        func()
    return wrapper

def chicken():
    print("Курица")

@bun
@cheese
@salad
def chicken_burger():
    chicken()

chicken_burger()
