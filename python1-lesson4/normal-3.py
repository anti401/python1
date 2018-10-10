# coding : utf-8

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random
import re

number = ''
for _ in range(2500):
    number += str(random.randint(0, 9))

with open('number2500.txt', 'w', encoding='UTF-8') as f:
    f.write(number)

lst = re.findall(r'[0]+|[1]+|[2]+|[3]+|[4]+|[5]+|[6]+|[7]+|[8]+|[9]+', number)
max_seq = ''
for seq in lst:
    if len(seq) > len(max_seq):
        max_seq = seq
print(max_seq)
