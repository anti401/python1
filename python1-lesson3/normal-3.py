# coding : utf-8

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func, lst):
    new_list = []
    for i in lst:
        if func(i):
            new_list.append(i)
    return new_list


test_data = [1, 2, 3, 4, 5]

print(my_filter(lambda x: x > 2, test_data))
