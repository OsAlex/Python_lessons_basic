# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

orig_list = [1, 2, 4, 0]

new_list = [i**2 for i in orig_list]
print(new_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list_a = ['a', 'b', 'c', 'd']
fruit_list_b = ['b', 'd', 'f', 'h']

fruit_list_cross = [i for i in fruit_list_a if i in fruit_list_b]
print(fruit_list_cross)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

lst = []
for el in range(33):
    lst.append(random.randint(-100, 100))

lst_div_3 = [i for i in lst if i % 3 == 0]
print(lst_div_3)

lst_positiv = [i for i in lst if i >= 0]
print(lst_positiv)

lst_ndiv_4 = [i for i in lst if i % 4 != 0]
print(lst_ndiv_4)


