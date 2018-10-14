# coding : utf-8

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

for i in range(1, 10):
    dir_name = 'dir_' + str(i)
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        print('Папка', dir_name, 'уже существует.')
    else:
        print('Папка', dir_name, 'успешно создана.')

input('Проверьте папки и введите что-нибудь, они будут удалены - ')

for i in range(1, 10):
    dir_name = 'dir_' + str(i)
    try:
        os.rmdir(dir_name)
    except FileNotFoundError:
        print('Папка', dir_name, 'не существует.')
    else:
        print('Папка', dir_name, 'успешно удалена.')
