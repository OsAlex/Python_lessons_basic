#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import os
import random

class Bochonok:
    """
    Объект-итератор
    """
    def __init__(self, amount=90):
        self.i = 1
        self.bochonki = [x for x in range(1,amount+1)]
        self.outed = []
    # Объект считается итератором - если у него есть метод __next__

    def __next__(self):
        self.i += 1
        if self.i <= 91:
        	y = random.randint(0, len(self.bochonki)-1)
        	bochonok = self.bochonki[y]
        	print(len(self.bochonki), len(self.outed))
        	self.outed.append(self.bochonki[y])
        	self.bochonki.remove(self.bochonki[y])
        	return bochonok
        else:
            raise StopIteration


class Meshochek:
    """
    Объект, поддерживающий интерфейс итерации
    """
    def __init__(self, amount=90):
        self.amount = amount

    def __iter__(self):
        # Метод __iter__ должен возвращать объект итератор
        return Bochonok(self.amount)

class Bilet(object):
	"""tring for Bilet"""
	def __init__(self, title):
		super(Bilet, self).__init__()
		self.title = title
		self.striked = []
		self.data = []
		for x in range(0,9):
			self.data.append([])
			self.data[x] = []
		for y in range(0,3):
			for x in range(0,9):
				self.data[x].append(self.getRanfom(x))
		for x in range(0,9):
			self.data[x].sort()

		self.all = []
		for x in range(0,9):
			self.all = self.all + self.data[x]

		print(self.all)
		
	def __str__(self):
		result = '{:-^40}'.format(self.title) + "\n"
		for y in range(0,3):
			for x in range(0,9):
				if self.data[x][y] in self.striked:
					result += '\033[4m' + '{:^4}'.format(self.data[x][y]) + '\033[0m'
				else:
					result += '{:^4}'.format(self.data[x][y])
			result += "\n"
		result += '-'*40 + "\n"

		return result

	def getRanfom(self,x):
		regen = True
		while regen:
			y = random.randint(x*10, (x+1)*10)
			y = 1 if y == 0 else y
			regen = False
			for d in range(0,9):
				if y in self.data[d]:
					regen = True
		return y

bilet_player = Bilet('Your bilet')
bilet_comp = Bilet('Computer bilet')
meshochek = Meshochek()
win = False

for bochonok in meshochek:
	print("\n"*100)
	print('New bochonok: ', bochonok)
	print(bilet_player)
	print(bilet_comp)
	print('Check bochonok?(y/n)')
	checks = ['y', 'n']
	check = ''
	while check not in checks:
		check = input()

	if check == 'y' and bochonok in bilet_player.all:
		bilet_player.striked.append(bochonok)

	if (check == 'y' and bochonok not in bilet_player.all) or (check == 'n' and bochonok in bilet_player.all):
			print('Game Over!')
			break;

	if bochonok in bilet_comp.all:   # computer never missed
		bilet_comp.striked.append(bochonok)

	if len(bilet_player.striked) == len(bilet_player.all):
		win = True
		break

	if len(bilet_comp.striked) == len(bilet_comp.all):
		break

if win:
	print('You WIN! Your prize aaaaaaaaaautomobile!')
else:
	print('You lose!')