# coding : utf-8

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    n = int(number * 10 ** ndigits * 10)
    if n % 10 < 6:
        return n // 10 / 10 ** ndigits
    else:
        return (n + 10) // 10 / 10 ** ndigits


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
