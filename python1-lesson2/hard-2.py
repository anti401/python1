# coding : utf-8

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

date = input('Введите дату в формате dd.mm.yyyy - ')

digits = set('0123456789')
err = False

# состав строки и положение точек
i = 0
while i < len(date):
    if i in (2, 5):
        if date[i] != '.':
            err = True
            break
    else:
        if date[i] not in digits:
            err = True
            break
    i += 1

day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:])

# проверка диапазонов
if day < 1 or day > 31:
    err = True
if month < 1 or month > 12:
    err = True
if year < 1 or year > 9999:
    err = True

if err:
    print('Дата некорректна!')
else:
    print('Дата корректна.')