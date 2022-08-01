# 6-Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# Полезная информация
# Допустим, у вас есть функция.
# def is_int(input_number:str):
# '''
# Проверяет аргумент на принадлежность к int
# params:input_number - введенное значение
# return: int или False
# '''
# try:
# input_number = int(input_number)
# return input_number
# except ValueError:
# return False
# Вы можете использовать эту функцию в лямбде. Делается это, примерно, вот так:
# ┌────────────────────────────┐
# │lambda input_number: is_int(input_number) │
# └────────────────────────────┘
# или даже необязательно называть это input_number:
# ┌────────────────┐
# │lambda char: is_int(char)│

def result():
    i = 0
    while i < 1:
        try: 
            i = int(input('Введите число: '))
        except ValueError:
            print('вы ввели не число')
    return i

def sequence(num):
    lst= list(map(lambda x: (-3) ** x, [exponent for exponent in range(num)]))
    return lst


print(sequence(result()))