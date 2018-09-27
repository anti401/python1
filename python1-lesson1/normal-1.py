# coding : utf-8

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.

number = int(input('Введите целое число: '))

max_digit = 0
while number > 0:
    if number % 10 > max_digit:
        max_digit = number % 10
    number //= 10

print('Самая большая цифра в вашем числе - ' + str(max_digit))
