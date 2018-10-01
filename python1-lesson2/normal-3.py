# coding : utf-8

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.

import random

n = int(input('Введите количество элементов списка: '))

random_list = []
i = 0
while i < n:
    random_list.append(random.randint(-100, 100))
    i += 1

print(random_list)