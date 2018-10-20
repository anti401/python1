# coding : utf-8
# детали задания в task.txt

import random


class Ticket:
    def __init__(self):
        # генерируем 15 случайных чисел
        numbers = set()
        while len(numbers) < 15:
            numbers.add(random.randint(1, 90))
        # сохраняем в отсортированном виде как список и кортеж
        self.numbers_list = list(numbers)
        self.numbers_list.sort()
        self.numbers_orig = tuple(self.numbers_list)

    def print_ticket(self):
        """Вывод карточки таблицей с прочерками"""
        numbers = [str(num).zfill(2) if num in self.numbers_list else ' -' for num in self.numbers_orig]
        for i in range(3):
            print(' '.join(numbers[i::3]))

    def __gt__(self, other):
        """Перегруженный оператор > для зачёркивания номера"""
        if other in self.numbers_list:
            self.numbers_list.remove(other)
            return True
        else:
            return False


user_ticket = Ticket()
comp_ticket = Ticket()

out_numbers = {0}
new_number = 0
operation = ''
while operation != 'q':
    # получаем новый уникальный номер
    while new_number in out_numbers:
        new_number = random.randint(1, 90)
    out_numbers.add(new_number)

    print('\nНовый бочонок: {}, осталось {} штук.'.format(new_number, 91 - len(out_numbers)))
    print('Ваша карточка:')
    user_ticket.print_ticket()
    print('Карточка компьютера:')
    comp_ticket.print_ticket()
    operation = input("Зачеркнуть цифру? (y/n/q) - ")

    # вычёркиваем номер на карточке компьютера
    comp_ticket > new_number

    # вычёркиваем номер на карточке игрока
    if operation == 'y' and not (user_ticket > new_number):
        print('Вы проиграли! (бочонка нет на вашей карточке)')
        break
    if operation == 'n' and user_ticket > new_number:
        print('Вы проиграли! (бочонок был на вашей карточке)')
        break
    if operation not in set('yn'):
        break

    # объявляем победителя, если чья-то карточка пуста
    if len(user_ticket.numbers_list) == 0 and len(comp_ticket.numbers_list) == 0:
        print('Ничья!')
        break
    if len(user_ticket.numbers_list) == 0:
        print('Победа ваша!')
        break
    if len(comp_ticket.numbers_list) == 0:
        print('Победа компьютера!')
        break
