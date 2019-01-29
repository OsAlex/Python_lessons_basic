# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")

    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def my_cp(file_name):
    '''
    создает копию указанного файла.

    Parameters
    ----------
    file_name : string filename which we copying.

    Raises
    ------
    ValueError : If file_name not exists.
    '''

    source = os.path.join(os.getcwd(), file_name)
    if os.path.exists(source) != True or os.path.isfile(source) != True:
        raise ValueError(f"Wrong parameter {file_name}: file not exists!")

    dest = source + '.copy'
    with open(source, 'r', encoding="utf-8") as src, open(dest, 'w', encoding="utf-8") as dst: dst.write(src.read())

def my_rm(file_name):
    '''
    удаляет указанный файл (запросить подтверждение операции).

    Parameters
    ----------
    file_name : string filename which we remove.

    Raises
    ------
    ValueError : If file_name not exists.
    '''

    file_path = os.path.join(os.getcwd(), file_name)
    if os.path.exists(file_path) != True or os.path.isfile(file_path) != True:
        raise ValueError(f"Wrong parameter {file_name}: file not exists!")

    os.remove(file_path)

def my_cd(path):
    '''
    меняет текущую директорию на указанную.

    Parameters
    ----------
    path : string name dir where we go.

    Raises
    ------
    ValueError : If path not exists.
    '''
    if os.path.exists(os.path.join(os.getcwd(), path)) != True:
        raise ValueError(f"Wrong parameter {path}: dir not exists!")

    dir_path = os.path.join(os.getcwd(), path)
    os.chdir(dir_path)

def my_ls():
    '''
    отображение полного пути текущей директории
    '''
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": my_cp,
    "rm": my_rm,
    "cd": my_cd,
    "ls": my_ls,
}

try:
    param = sys.argv[2]
except IndexError:
    param = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    if key and do.get(key):
        if param:
            do[key](param)
        else:
            do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
except Exception as e:
    print(f"Something wrong with command {key}({param}) - {e}")


