# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    celoe, drobnoe = str(number).split('.')

    okruglenie = i = 0
    for cifra in drobnoe[::-1]:
        i += 1

        if int(cifra) + okruglenie > 4:
            okruglenie = 1

        if i >= ndigits:
            break

    last_cifra = int(drobnoe[i-1]) + okruglenie

    next = 0
    res = [last_cifra] + list(drobnoe[-(ndigits - 1):-(len(drobnoe) + 1):-1])

    if last_cifra > 9:
        for i in range(len(res)):
            res[i] = int(res[i]) + next

            if int(res[i]) + next > 9:
                res[i] = 0
                next = 1
            else:
                next = 0

    if next == 1:
        celoe = int(celoe) + 1

    return float(str(celoe) + '.' + ''.join([str(i) for i in res[::-1]]))


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    return sum(list(map(int, list(str(ticket_number)[:3])))) == sum(list(map(int, list(str(ticket_number)[3:]))))

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
