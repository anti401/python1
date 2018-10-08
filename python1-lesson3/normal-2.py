# coding : utf-8

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    i = 0
    while i < len(origin_list) - 1:
        if origin_list[i] > origin_list[i + 1]:
            origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
            if i > 0:
                i -= 2
        i += 1
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
