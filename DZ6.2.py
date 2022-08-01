# 2- Найти сумму чисел списка стоящих на нечетной позиции

num_list = []
for element in input('Введите числа через пробел: ').split():
    num_list.append(int(element))

print(num_list)


def sum_list(ls):
    sum = 0
    for i in enumerate(ls):
        if i[1] % 2 != 0:
            sum = sum + i[1]
    return sum

print('Cумма чисел на нечетных позициях: ', sum_list(num_list))