'''
Task_4_1
Собрать с помощью декораторов гамбургер:
- булка
- лук
- помидоры
- говядина
- булка
'''

def bun(func):
    def wrapper():
        print("Булка")
        func()
        print("Булка")
    return wrapper

def onion(func):
    def wrapper():
        print("Лук")
        func()
    return wrapper

def tomato(func):
    def wrapper():
        print("Помидоры")
        func()
    return wrapper

def beef():
    print("Говядина")

@bun
@onion
@tomato
def hamburger():
    beef()

hamburger()
