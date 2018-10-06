# coding : utf-8

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


def nod(x, y):
    # наибольший общий делитель
    while y != 0:
        x, y = y, x % y
    return x


def fractal_add(a, b):
    # сложение двух дробей
    res = [0, 1]
    res[1] = a[1] * b[1]
    res[0] = a[0] * b[1] + b[0] * a[1]
    d = nod(abs(res[0]), res[1])
    return list(map(lambda n: n // d, res))


# реализовано для любого количества операций в строке
formula = input('Введите выражение: ')
formula = formula.replace('  ', ' ').replace(' /', '/').replace('/ ', '/')
lexems = formula.split(' ')

result = [0, 1]
number = [0, 1]
current_operation = '+'
i = 0
while i < len(lexems):
    # текущая операция
    if lexems[i] == '+':
        current_operation = '+'
    elif lexems[i] == '-':
        current_operation = '-'
    else:
        # извлекаем число
        if '/' in lexems[i]:
            number[0] = int(lexems[i].split('/')[0])
            number[1] = int(lexems[i].split('/')[1])
        elif i == len(lexems) - 1 or '/' not in lexems[i + 1]:
            number[0] = int(lexems[i])
            number[1] = 1
        else:
            number[1] = int(lexems[i + 1].split('/')[1])
            number[0] = int(lexems[i]) * number[1] + int(lexems[i + 1].split('/')[0])
            i += 1
        # производим операцию
        if current_operation == '+':
            result = fractal_add(result, number)
        else:
            number[0] *= -1
            result = fractal_add(result, number)
    i += 1

if result[0] >= 0:
    if result[0] % result[1] == 0:
        print('Результат: {}'.format(result[0] // result[1]))
    else:
        print('Результат: {} {}/{}'.format(result[0] // result[1], result[0] % result[1], result[1]))
else:
    if result[0] % result[1] == 0:
        print('Результат: {}'.format(abs(result[0]) // result[1]))
    else:
        print('Результат: -{} {}/{}'.format(abs(result[0]) // result[1], abs(result[0]) % result[1], result[1]))
