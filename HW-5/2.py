'''
Написать функцию count_char, которая принимает строковое значение
STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
'буква': количество-вхождений-в-строку
}
например: {
'p': 2,
'y': 1,
}
STR_VAL = 'python is the fastest-growing major programming language'
Нельзя пользоваться collections.Counter!
'''

# Инициализация функции  count_char
def count_char(STR_VAL):
    char_count = {}  # Создаем пустой словарь для подсчета вхождений букв
    for char in STR_VAL:
        if char.isalpha():  # Проверяем, является ли символ буквой
            char = char.lower()  # Приводим букву к нижнему регистру для учета регистра (если заглавная)
            char_count[char] = char_count.get(char, 0) + 1  # Увеличиваем счетчик вхождений буквы
    return char_count

STR_VAL = 'python is the fastest-growing major programming language'

# Вызываем функцию count_char
print(count_char(STR_VAL))
