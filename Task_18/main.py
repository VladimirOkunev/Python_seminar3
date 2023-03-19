# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
import math

lengh = int(input('Введите число элементов массива: '))

num_list = [random.randint(0,20) for _ in range(lengh)]

print(num_list)

value = int(input('Введите значение числа X: '))

diff = math.fabs(num_list[0] - value)

for i in range(len(num_list)):
    if math.fabs(num_list[i] - value) <= diff:
        diff = math.fabs(num_list[i] - value)
        index = i
print(f'Ближайшее значание к числу {value} -> {num_list[index]}')