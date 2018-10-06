# coding : utf-8

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os

chars = set()
orig_path = os.path.join('data', 'fruits.txt')
with open(orig_path, 'r', encoding='UTF-8') as f:
    for line in f:
        if line == '\n':
            continue
        if line[0].upper() not in chars:
            chars.add(line[0].upper())
            new_path = os.path.join('data', 'fruits_' + line[0].upper() + '.txt')
            with open(new_path, 'w', encoding='UTF-8') as new_f:
                new_f.write(line)
        else:
            new_path = os.path.join('data', 'fruits_' + line[0].upper() + '.txt')
            with open(new_path, 'a', encoding='UTF-8') as new_f:
                new_f.write(line)
