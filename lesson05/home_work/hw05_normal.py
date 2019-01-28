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
import hw05_easy as my_file_func

menu = [
    '1. Перейти в папку',
    '2. Просмотреть содержимое текущей папки',
    '3. Удалить папку',
    '4. Создать папку',
]

while(True):
    for item in menu:
        print(item)

    try:
        selected = int(input())
    except Exception:
        print('Good Bay!')
        break

    if selected == 1 or selected == 3 or selected == 4:
        print('Input dir name: ')
        dirname = input()

    if selected == 1:
        try:
            os.chdir(dirname)
        except Exception as e:
            print('Something wrong with chdir ' + str(dirname) + ': ' + str(e))
    elif selected == 2:
        my_file_func.print_dirs()
    elif selected == 3:
        my_file_func.remove_dir(dirname)
    elif selected == 4:
        my_file_func.create_dir(dirname)
