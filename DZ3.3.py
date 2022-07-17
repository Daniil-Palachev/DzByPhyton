# 3 - Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.567, 10.03] => 0.564 или 564 

lst = [1.1, 1.2, 3.1, 5.567, 10.03]

def get_two_after_point(number: float) -> float:
    return round(number - int(number), 3)


def get_difference(lst: list) -> float:
    minnum = get_two_after_point(lst[0])
    maxnum = get_two_after_point(lst[0])
    for i in lst:
        maxnum = max(maxnum, get_two_after_point(i))
        minnum = min(minnum, get_two_after_point(i)) 
    return round(maxnum - minnum, 3)


dif = get_difference(lst)
print(dif)