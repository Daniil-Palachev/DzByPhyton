# При решении не забывайте, пожалуйста, про функции: каждая задача должна быть представлена в виде одной или цепочки функции
# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

text= 'абвгдейка - это передача'
a= input('Введите буквы: ')


def without_abv(alphabet: str, text1: str):
    text1 = text1.split()
    lst= ''
    for i in text1:
        if not i.count(alphabet):
            lst+=i+ ' '
    return lst



result = without_abv(a,text)
print(result)

















