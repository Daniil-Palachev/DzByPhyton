# 3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

def IntTest(text):

    test = True
    while test:
        a = input(f"{text}")
        if a.isdigit():
            a = int(a)
            if a <= 0:
                print("нужно число > 0")
            else:
                test = False
        else:   
            print("НУЖНО ВВЕСТИ ИМЕННО ЧИСЛО!!")
    return a

n = IntTest("Введите число : ")

lib = {}
for i in range(1,n+1):
    lib[i] = (1+1/i)**i
print(lib)

res = 0
for i in lib:
    res += round(lib[i])
print(res)