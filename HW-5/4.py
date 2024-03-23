'''
С помощью декораторов реализовать конвейер сборки бургера
Написать декоратор bread, который:
- до декорируемой функции будет печатать
"</------------\\>"
- после декорируемой функции будет
печатать "<\\____________/>"
Написать декоратор tomato, который:
- до декорируемой функции будет печатать
"*** помидоры ****"
Написать декоратор salad, который:
- до декорируемой функции будет
печатать "~~~~ салат ~~~~~"
Написать декоратор cheese, который:
- до декорируемой функции будет
печатать "^^^^^ сыр ^^^^^^"
Написать декоратор onion, который:
- до декорируемой функции будет
печатать "----- лук ------"
Написать функцию beef, которая:
- печатает "### говядина ###"
Написать функцию chicken, которая:
- печатает "|||| курица ||||"
'''

def bread(func):
    def wrapper():
        print("</------------\\\\>")
        func()
        print("<\\\\____________/>")
    return wrapper

def tomato(func):
    def wrapper():
        print("*** помидоры ****")
        func()
    return wrapper

def salad(func):
    def wrapper():
        print("~~~~ салат ~~~~~")
        func()
    return wrapper

def cheese(func):
    def wrapper():
        print("^^^^^ сыр ^^^^^^")
        func()
    return wrapper

def onion(func):
    def wrapper():
        print("----- лук ------")
        func()
    return wrapper

def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_decorator
def beef():
    print("### говядина ###")

@log_decorator
def chicken():
    print("|||| курица ||||")

# Декорируем функцию beef
beef = bread(beef)
beef = tomato(beef)
beef = salad(beef)
beef = cheese(beef)
beef = onion(beef)

# Декорируем функцию chicken
chicken = bread(chicken)
chicken = tomato(chicken)
chicken = salad(chicken)
chicken = cheese(chicken)
chicken = onion(chicken)

# Выводим на экран
beef()
print()
chicken()
