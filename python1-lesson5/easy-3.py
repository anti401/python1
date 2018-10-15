# coding : utf-8

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys

with open(sys.argv[0], 'r', encoding='UTF-8') as f:
    file_lines = f.readlines()

with open(sys.argv[0] + '__copy', 'w', encoding='UTF-8') as f:
    f.writelines(file_lines)
