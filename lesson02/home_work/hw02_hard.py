
__author__ = 'Осипов Алексей Петрович'

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

print("\n#1:\n")

import re

match = re.search('([0-9\-]+)x', equation)
k = float(match.group(1))

match = re.search('\+\s([\d\.\-]+)', equation)
b = float(match.group(1))

y = k * x + b
print(y)


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

dates = []
# Пример корректной даты
dates.append('01.11.1985')

# Примеры некорректных дат
dates.append('01.22.1001')
dates.append('1.12.1001')
dates.append('-2.10.3001')

print("\n#2:\n")

for date in dates:
    day, month, year = date.split('.')

    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        print('wrong')
        continue

    day, month, year = [int(day), int(month), int(year)]

    if ((month % 2 == 0) and (day < 1 or day > 30)) or ((month % 2 != 0) and (day < 1 or day > 31)):
        print('wrong')
        continue

    if month not in range(1, 12):
        print('wrong')
        continue

    if year not in range(1, 9999):
        print('wrong')
        continue

    print('correct')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

print("\n#3:\n")

print('Input room number: ')
needRoom = abs(int(input()))
indexLevelRepeat = level = room = 0

while room < needRoom:
    indexLevelRepeat = indexLevelRepeat + 1
    for repeatLevel in range(indexLevelRepeat):
        for indexRoom in range(indexLevelRepeat):
            room = room + 1
            # print(f'Level: {level} room: {room} i: {i} j: {repeatLevel} jj: {indexRoom}')

            if room >= needRoom:
                break

        level = level + 1

        if room >= needRoom:
            break

# print(f'Level number: {level} index room on level: {indexRoom + 1}')
print(level, indexRoom + 1)