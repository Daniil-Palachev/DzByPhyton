# 4 - Реализуйте  алгоритм перемешивания списка

import time
a = str(time.time_ns())
lst = [7,9,8,4]
print(lst)
for i in range(0,len(lst)):
    for j in a:
        if int(j) < len(lst):
            lst[i],lst[int(j)] = lst[int(j)],lst[i]
print(lst)