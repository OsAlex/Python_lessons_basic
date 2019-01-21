# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

import re

def sum_drobi(str_input):

    [(one_drob_up, one_drob_down, znak, two_drob_up, two_drob_down)] = re.findall(r"(\-?\d)\/?(\d?)\s+([\-\+]+)\s+(\-?\d)\/?(\d?)", str_input)
    znak = int(znak + '1')

    one_drob_down = one_drob_down if len(one_drob_down) > 0 else 1
    two_drob_down = two_drob_down if len(two_drob_down) > 0 else 1

    # print(one_drob_up, one_drob_down, znak, two_drob_up, two_drob_down)

    result_up = int(one_drob_up) * int(two_drob_down) + znak * (int(two_drob_up) * int(one_drob_down))
    znamenatel = int(one_drob_down) * int(two_drob_down)
    celoe = result_up // znamenatel

    if abs(celoe) > 0:
        result_up = abs(result_up) - abs(celoe) * znamenatel

    print(celoe, result_up, znamenatel)

    a = result_up
    b = znamenatel
    while b != 0:
        a, b = b, a % b

    result_up = int(result_up / a)
    znamenatel = int(znamenatel / a)

    return str(celoe) + str(result_up) + '/' + str(znamenatel)

print(sum_drobi('-5 + -4/7'))
print(sum_drobi('-2/3 - -2'))


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
