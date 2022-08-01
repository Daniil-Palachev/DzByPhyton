# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint
from functools import reduce


num_list= [2, 3, 4, 5, 6]

def result(lst):
    res_list = []
    first_i = 0
    last_i = len(lst) - 1
    while last_i - first_i >= 0:
        res_list.append(reduce(lambda x, y: x * y, [lst[first_i], lst[last_i]]))
        first_i += 1
        last_i -= 1
    return res_list


print(num_list)
print(result(num_list)) 



