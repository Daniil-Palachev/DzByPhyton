# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11


def IntTest(text):

    test = True
    minus = False
    while test:
        a = input(f"{text}")
        if a[0] == "-":
            minus = True
            a = a.replace("-","")
        if a.isdigit():
            a = int(a)
            if minus:
                a = a*(-1)
            test = False
        else :
            print("НУЖНО ВВЕСТИ ИМЕННО ЧИСЛО!!")
    return a

n = str(IntTest("Введите число : "))
res = 0
for i in n:
    if i.isdigit():
        res = res+int(i)

print(res) 


