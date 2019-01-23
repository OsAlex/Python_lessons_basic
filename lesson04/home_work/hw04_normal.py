# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

import re

with_re = re.findall(r'([a-z]+)[A-Z]+([a-z]+)', line) # если брать только символы вокруг символов в верхнем регистре
lst = [j for i in with_re for j in i]
print(lst)

with_re = re.findall(r'[a-z]+', line) # просто все символы в нижнем регистре, тоже даёт верное решение
print(with_re)

temp = ''
result = []

for symbol in line:
       if ord(symbol) in range(ord('a'), ord('z')):
              temp = temp + symbol
       if ord(symbol) in range(ord('A'), ord('Z')) and len(temp) > 0:
              result.append(temp)
              temp = ''

if len(temp) > 0:
       result.append(temp)

print(result)

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

import re

with_re = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2)
print(with_re)

line_2 = 'GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec'
print(line_2)

with_re = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2)
print(with_re)

temp = ''
result = []
small_count = 0
big_count = 0

for symbol in line_2:
       #print(symbol, small_count, big_count, temp)
       if ord(symbol) in range(ord('a'), ord('z')+1):
              # закончились большие буквы, их было нужное кол-во и перед ними было нужное кол-во маленьких
              if big_count > 2 and small_count == -1:
                     result.append(temp[:big_count-2])
                     temp = ''

              # сброс флага маленьких букв, когда после больших начались снова маленькие буквы
              if small_count == -1:
                     small_count = 0
              small_count += 1
              big_count = 0
              temp = ''

       if ord(symbol) in range(ord('A'), ord('Z')+1):
              big_count += 1
              # установка флага маленьких букв, если перед большими было достаточное количество маленьких букв
              # или сброс
              if small_count >= 2 or small_count == -1:
                     small_count = -1
              else:
                     small_count = 0
              temp = temp + symbol

print(result)


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random

with open('bigChislo.txt', 'w', encoding='UTF-8', ) as f:
       f.write('')

i = 0
while i < 2500:
       i += 1
       cifra = random.randint(0,9)
       with open('bigChislo.txt', 'a', encoding='UTF-8', ) as f:
              f.write(str(cifra))

repeated = {}
prev_cifra = None
current_repeat = 0
is_repeat = False

with open('bigChislo.txt', 'r', encoding='UTF-8') as f:
    for line in f:
       for cifra in line:
              #print(cifra, prev_cifra, is_repeat, current_repeat)
              if prev_cifra == cifra:
                     if is_repeat:
                            repeated[current_repeat].append(cifra)
                     else:
                            is_repeat = True
                            repeated[current_repeat] = []
                            repeated[current_repeat].append(cifra)
                            repeated[current_repeat].append(cifra)
              else:
                     if is_repeat:
                            is_repeat = False
                            current_repeat += 1
              prev_cifra = cifra

count_repeated = [[len(values), values[0]] for values  in repeated.values()]

max_key, max_values = max(count_repeated)
max_count_repeated = [[i, j] for [i, j] in count_repeated if i == max_key]

print('самые длинные последовательности одинаковых цифр:')
i = 0
for key, val in max_count_repeated:
       i += 1
       print(str(i)+')', key * val)






