# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

# https://zen.yandex.ru/suite/a6424a0f-4fdb-44a1-95a0-9945e6f0a699
# Это на случай возникновения непонятных символов в файле.


file_name= 'C:\\Users\\админ\\Desktop\\ДЗ\\python\\DZ\\new_text.txt'
file = open(file_name, 'w', encoding='utf-8')
file.write('Мама сшила м0не штаны и7з бере9зовой кор45ы 893.')
file.close()


def del_num(file_name):
    file = open(file_name, 'r', encoding="utf-8")
    text = file.readline().split()
    file.close()
    text1 = ''
    print(text)
    for i in text:
        if not is_has_digit(i):
            text1 += i + ' '
    print(text1)


def is_has_digit(text):
    for c in text:
        if c.isdigit():
            return True
    return False


del_num(file_name)