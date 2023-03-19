# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

lengh = int(input('Введите число элементов массива: '))

value = int(input('Введите значение числа X: '))

count = 0

num_list = [random.randint(0,20) for _ in range(lengh)]

print(num_list)

for i in range(len(num_list)):
    if num_list[i] == value:
        count += 1

print(f'Число {value} встречается {count} раз')
