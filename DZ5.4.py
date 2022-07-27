# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# При декодировании попробуйте сделать через четный-нечетный элемент.

from itertools import groupby

def read_text(words: str):
    with open(words, 'r', encoding='utf-8') as file:
        result = file.read()
    return result

def zip_data(text: str):
    out = "".join([f"{i}{len(list(j))}" for i, j in groupby(text)])
    with open('C:\\Users\\админ\\Desktop\\ДЗ\\python\\DZ\\out.txt', 'w', encoding='utf-8') as file:  
        file.write(out)
    return out

def zip_file(text: str):
    lst = "".join(" " if i.isdigit() else i for i in text).split() 
    num = "".join(i if i.isdigit() else " " for i in text).split()  
    zip_text = ''.join([x * y for x, y in zip(lst, map(int, num))])
    return zip_text

def res():
    input_str = read_text('C:\\Users\\админ\\Desktop\\ДЗ\\python\\DZ\\vhod.txt')
    print('Текст:', input_str)
    zip = zip_data(input_str)
    print('Результат сжатия:', zip)
res()