# coding : utf-8

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


def clear_split(line):
    # разбор строки по словам
    s = line.strip()
    while s.find('  ') != -1:
        s = s.replace('  ', ' ')
    return s.split(' ')


humans = {}
with open('workers.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        data = clear_split(line)
        if data[2] == 'Зарплата':
            continue
        name = data[0] + ' ' + data[1]
        humans[name] = [int(data[2]), int(data[4]), 0, 0]

with open('hours_of.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        data = clear_split(line)
        if data[2] == 'Отработано':
            continue
        name = data[0] + ' ' + data[1]
        humans[name][2] = int(data[2])
        humans[name][3] = int(humans[name][0] * humans[name][2] / humans[name][1])
        if humans[name][2] > humans[name][1]:
            humans[name][3] += humans[name][3] - humans[name][0]

print('{:>20}{:>10}{:>10}{:>10}{:>10}'.format('Имя сотрудника', 'Оклад', 'Норма(ч)', 'Факт(ч)', 'Зарплата'))
for name, data in humans.items():
    print('{:>20}{:>10}{:>10}{:>10}{:>10}'.format(name, data[0], data[1], data[2], data[3]))
