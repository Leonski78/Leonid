''' Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X'''

import random
 
N = int(input('Введите число N: '))
array = [random.randint(1, 10) for _ in range(N)]
print(array)
X = int(input('Введите число X: '))
count = 0
index = 0
min = X - array[0]
for i in range(0, len(array)):
    count = X - array[i]
    if count < min:
        min = count
        index = i
print (f'{array[index]} ближайшее число в массиве к числу {X}')