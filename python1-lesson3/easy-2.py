# coding : utf-8

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    str_number = str(ticket_number).zfill(6)
    s = 0
    i = 0
    while i < len(str_number):
        if i < len(str_number) // 2:
            s += int(str_number[i])
        else:
            s -= int(str_number[i])
        i += 1
    return s == 0


print(lucky_ticket(123006))
print(lucky_ticket(12321))  # рассматриваем как 012321
print(lucky_ticket(436751))
