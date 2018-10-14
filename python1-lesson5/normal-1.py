# coding : utf-8

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import easy_lib as ez

current_dir = os.getcwd()
operation = ''
while operation != 'q':
    print('\nДоступные операции:')
    print('1. Перейти в папку')
    print('2. Просмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')
    operation = input("Введите номер операции или 'q' для выхода - ")

    if operation == '1':
        aim_dir = input("Введите имя папки для перехода - ")
        if os.path.isdir(os.path.join(current_dir, aim_dir)):
            current_dir = os.path.join(current_dir, aim_dir)
            print('Переход выполнен успешно.')
        else:
            print('Переход невозможен.')

    elif operation == '2':
        print(os.listdir(current_dir))

    elif operation == '3':
        del_dir = input("Введите имя папки для удаления - ")
        ez.delete_dir(os.path.join(current_dir, del_dir))

    elif operation == '4':
        new_dir = input("Введите имя новой папки - ")
        ez.make_dir(os.path.join(current_dir, new_dir))

    else:
        print('Неизвестный номер операции.')
