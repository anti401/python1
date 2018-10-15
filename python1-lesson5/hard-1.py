# coding : utf-8

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.


import os
import sys
import shutil as sh

# ***********************************************************************
# sys.argv.append('ls')

# sys.argv.append('cp')
# sys.argv.append('easy-1.py')

# sys.argv.append('rm')
# sys.argv.append('easy-1.py__copy')

# print('sys.argv = ', sys.argv)
# ***********************************************************************


def copy_file():
    """Копирование файла"""
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        dir_path = os.path.join(os.getcwd(), dir_name)
        sh.copyfile(dir_path, dir_path + '__copy')
    except FileNotFoundError:
        print('Файл не найден.')
    except FileExistsError:
        print('Копия уже существует.')
    else:
        print('Файл успешно скопирован.')


def delete_file():
    """Удаление файла"""
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    perm = input('Подтвердите удаление вводом "y" - ')
    if perm == 'y':
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.remove(dir_path)
        except FileNotFoundError:
            print('Файл не существует.')
        else:
            print('Файл успешно удалён.')


def print_path():
    """Вывод полного пути до папки"""
    print('Текущая папка:', os.getcwd())


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - копирование файла")
    print("rm <file_name> - удаление файла")
    print("ls - вывод полного пути до текущей папки")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": delete_file,
    "ls": print_path
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
