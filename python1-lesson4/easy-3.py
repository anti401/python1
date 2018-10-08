# coding : utf-8

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

lst = [random.randint(-10, 10) for _ in range(10)]
print('Исходный список: ', lst)

new_lst = [el for el in lst if el % 3 == 0]
print('Элементы, кратные 3: ', new_lst)

new_lst = [el for el in lst if el >= 0]
print('Положительные элементы: ', new_lst)

new_lst = [el for el in lst if el % 4 != 0]
print('Элементы, не кратные 4: ', new_lst)
