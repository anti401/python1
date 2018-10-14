# coding : utf-8

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

# список папок и файлов
c_dir = os.getcwd()
dir_files = os.listdir(c_dir)

# выводим только папки
for dir_candidate in dir_files:
    if os.path.isdir(os.path.join(c_dir, dir_candidate)):
        print(dir_candidate)
