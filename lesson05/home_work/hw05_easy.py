# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def create_dir(dirname):
    try:
        os.mkdir(dirname)
    except Exception:
        print('Something wrong with create ' + dirname)


def create_dirs():
    for i in range(1,10):
        create_dir('dir_' + str(i))

def remove_dir(dir):
    try:
        os.rmdir(dir)
    except Exception:
        print('Something wrong with remove ' + dir)

def remove_dirs():
    for i in range(1,10):
        remove_dir('dir_' + str(i))


create_dirs()
remove_dirs()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def print_dirs():
    for item in os.listdir():
        if os.path.isdir(item):
            print(item)

create_dirs()
print_dirs()
remove_dirs()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(source, dest):
    with open(source, 'r', encoding="utf-8") as src, open(dest, 'w', encoding="utf-8") as dst: dst.write(src.read())

copy_file(os.path.basename(__file__), os.path.basename(__file__) + '.copy')
