#4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Введите номер четверти: "))
if (quarter == 1):
    print('координаты должны быть введены в диапазоне: x > 0, y > 0')
elif (quarter == 2):
    print('координаты должны быть введены в диапазоне: x < 0, y > 0')
elif (quarter == 3):
    print('координаты должны быть введены в диапазоне: x < 0, y < 0')
elif (quarter == 4):
    print('координаты должны быть введены в диапазоне: x > 0, y < 0')
elif (quarter > 4):
    print('введен некоректный номер четверти') 

