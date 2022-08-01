# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def result():
    input_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
    search_string = "йцу"
    print(get_second_match(input_list, search_string))


def get_second_match(list_where_find, obj_to_find):
    if len(list(filter(lambda x: x == obj_to_find, list_where_find))) < 2: 
        print('Второго вхождения нет') 
    else:
        return list(filter(lambda x: x[1] == obj_to_find, list(enumerate(list_where_find))))[1][0]

result()