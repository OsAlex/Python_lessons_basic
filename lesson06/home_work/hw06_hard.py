# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os
import re


class Worker(object):
    """docstring for Worker"""

    def __init__(self, data):
        super(Worker, self).__init__()
        res = re.findall(r"(\S+)\s+(\S+)\s+(\d+)\s+(\S+)\s+(\d+)", data)
        if len(res) > 0:
            [name, family, salary, position, norm_hours] = res[0]
            self.name = name
            self.family = family
            self.salary = int(salary)
            self.position = position
            self.norm_hours = int(norm_hours)


workers = []
with open(os.path.join('data', 'workers'), 'r', encoding='UTF-8') as f:
    for line in f:
        res = re.findall(r"(\S+)\s+(\S+)\s+(\d+)\s+(\S+)\s+(\d+)", line)
        if len(res) > 0:
            workers.append(Worker(line))

with open(os.path.join('data', 'hours_of'), 'r', encoding='UTF-8') as f:
    for line in f:
        res = re.findall(r"(\S+)\s+(\S+)\s+(\d+)", line)
        if len(res) > 0:
            [name, family, work_hours] = res[0]
            worker = [x for x in workers if x.name == name and x.family == family][0]
            worker.work_hours = int(work_hours)

for worker in workers:
    salary_out = worker.salary
    if worker.work_hours - worker.norm_hours > 0:
        salary_out = salary_out + 2 * (worker.salary / worker.norm_hours) * (worker.work_hours - worker.norm_hours)
    if worker.work_hours - worker.norm_hours < 0:
        salary_out = salary_out - (worker.salary / worker.norm_hours) * (worker.norm_hours - worker.work_hours)
    print(worker.family, worker.name, salary_out)
