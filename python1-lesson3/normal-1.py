# coding : utf-8

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    fib = [1, 1]
    i = 2
    while i <= m:
        fib.append(fib[-1] + fib[-2])
        i += 1
    return fib[n-1:m]


print(fibonacci(4, 15))
