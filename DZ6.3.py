# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)
nums = str(input('Введите числа через пробел: '))

def result(numbers: str):
   x1,y1,x2,y2 = list(map(int ,numbers.split()))
   return ((x2-x1)**2 + (y2-y1)**2)**0.5

print(result(nums))