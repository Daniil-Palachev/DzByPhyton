# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/sH87m)

n = int(input("Введите число: "))

def pos_num_fibonacci(num: int) -> list:
    fibo = [0,1]
    for i in range(1, num):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo

def neg_num_fibonacci(num: int) -> list:
    fibo = [0,1]
    for i in range(1, num):
        fibo.append(fibo[-2] - fibo[-1])
    return fibo   

res = neg_num_fibonacci(n)[::-1]+ pos_num_fibonacci(n) 
print(res)