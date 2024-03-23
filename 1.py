class Calculator:
    def add(self, x, y):
        """Метод для сложения двух чисел"""
        return x + y

    def subtract(self, x, y):
        """Метод для вычитания одного числа из другого"""
        return x - y

    def multiply(self, x, y):
        """Метод для умножения двух чисел"""
        return x * y

    def divide(self, x, y):
        """Метод для деления одного числа на другое"""
        if y == 0:
            raise ValueError("Деление на ноль недопустимо")
        return x / y

# Пример использования класса калькулятора
calc = Calculator()

# Сложение
print("Сумма:", calc.add(5, 3))  # Вывод: 8

# Вычитание
print("Разность:", calc.subtract(10, 4))  # Вывод: 6

# Умножение
print("Произведение:", calc.multiply(6, 7))  # Вывод: 42

# Деление
print("Частное:", calc.divide(20, 5))  # Вывод: 4
