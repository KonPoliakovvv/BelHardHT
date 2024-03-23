'''
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
'''


# Инициализация функции  yes_or_no
def yes_or_no(numbers):
    seen_numbers = set()  # Множество для отслеживания уникальных чисел
    for num in numbers:
        if num in seen_numbers:
            print("Yes")
        else:
            print("No")
            seen_numbers.add(num)  # Добавляем число в множество

# Список производных чисел
numbers = [5, 1, 3, 1, 4, 2, 2, 3]

# Вызываем функцию yes_or_no
yes_or_no(numbers)
