#2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("Введи 0 или 1 для x: "))
y = int(input("Введи 0 или 1 для y: "))
z = int(input("Введи 0 или 1 для z: "))
left = not (x or y or z)
right = not x and not y and not z
res = left == right
print (res)