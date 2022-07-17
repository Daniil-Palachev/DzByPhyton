# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
n = int(input("Введите число: "))
def make_bin_num(number: int) -> str:
    bin_num = ''
    while number > 0:
        bin_num += str(number % 2)
        number //= 2
    return bin_num

res = make_bin_num(n)
print(res)
