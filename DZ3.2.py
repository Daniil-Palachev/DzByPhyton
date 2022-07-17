# 2 - Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst1 = [2, 3, 4, 5, 6]
lst2 = [2, 3, 5, 6]
def mult_of_pairs(lst: list) -> list:
    result = []
    first_index = 0
    last_index = len(lst) - 1
    while last_index - first_index >= 0:
        result.append(lst[first_index] * lst[last_index])
        first_index += 1
        last_index -= 1
    return result

mult1 = mult_of_pairs(lst1)
print(mult1)
mult2 = mult_of_pairs(lst2)
print(mult2)