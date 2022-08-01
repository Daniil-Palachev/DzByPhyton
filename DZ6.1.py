# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение
# Формат: Объясняет преподаватель

# Задача: предложить улучшения кода для уже решённых задач:

# - С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce

# 1- Определить, присутствует ли в заданном списке строк, некоторое число



lst_for_looking = input('Введите исходную строку: ')
num_what_looking_for = input('Введите искомое число: ')
    


def find_num(lst, num):
    return any(filter(lambda element: str(num) in element, lst))

print(find_num(lst_for_looking,num_what_looking_for))


