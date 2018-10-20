# coding : utf-8

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import re


class Worker:
    def __init__(self, line_from_file):
        w_data = re.findall(r'\d+|\w+', line_from_file)
        self.name = w_data[0] + ' ' + w_data[1]
        self.salary = int(w_data[2])
        self.plan_hours = int(w_data[4])
        self.fact_hours = 0
        self.to_pay = 0

    def calc_pay(self, fact_hours):
        self.fact_hours = fact_hours
        self.to_pay = int(self.salary * self.fact_hours / self.plan_hours)
        if self.fact_hours > self.plan_hours:
            self.to_pay += self.to_pay - self.salary


workers = []
with open('workers.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        if line.find('Зарплата') != -1:
            continue
        workers.append(Worker(line))

with open('hours_of.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        data = re.findall(r'\d+|\w+', line)
        if data[2] == 'Отработано':
            continue
        name = data[0] + ' ' + data[1]
        for w in workers:
            if w.name == name:
                w.calc_pay(int(data[2]))
                break

print('{:>20}{:>10}{:>10}{:>10}{:>10}'.format('Имя сотрудника', 'Оклад', 'Норма(ч)', 'Факт(ч)', 'Зарплата'))
for w in workers:
    print('{:>20}{:>10}{:>10}{:>10}{:>10}'.format(w.name, w.salary, w.plan_hours, w.fact_hours, w.to_pay))
