# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

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

lst = [1]
for i in range(1,n):
    lst.append(lst[i-1]*(i+1))
print(lst)
