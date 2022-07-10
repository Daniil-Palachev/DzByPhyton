#2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("Введи 0 или 1 для x: "))
y = int(input("Введи 0 или 1 для y: "))
z = int(input("Введи 0 или 1 для z: "))
res = True
for x in True, False:
    for y in True, False:
        for z in True, False:
            res = res and (not(x or y or z) == (not x and not y and not z))

print (res)