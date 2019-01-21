# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    def getFibo(y):
        res = []
        x = 0
        res.append(1)
        res.append(1)
        while x < y:
            x += 1
            res.append(res[x-2] + res[x-1])

        return res[x]

    result = []
    result.append(getFibo(n))

    i = 1
    result.append(getFibo(n+i))

    while n+i < m:
        i += 1
        result.append(result[i-2] + result[i-1])

    print(result)

fibonacci(1, 4)
fibonacci(20, 30)
fibonacci(2, 10)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):

    def popolam_filter(list_f, middle):
        left_list = []
        right_list = []

        for i in range(len(list_f)):
            if i != middle:
                if list_f[i] <= list_f[middle]:
                    left_list.append(list_f[i])
                elif list_f[i] > list_f[middle]:
                    right_list.append(list_f[i])

        return left_list, right_list

    def popolam(input_list):
        length = len(input_list)
        if length > 1:
            middle = int(length / 2)
            left_list, right_list = popolam_filter(input_list, middle)

            length = len(left_list)
            if length > 1:
                left_list = popolam(left_list)

            length = len(right_list)
            if length > 1:
                right_list = popolam(right_list)

            result = left_list + [input_list[middle]] + right_list
        else:
            result = input_list

        return result

    return popolam(origin_list)

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(function, input_list):
    result = []
    for element in input_list:
        if function(element):
            result.append(element)

    return result

print(my_filter(lambda x: x % 2 == 0, [0, 1, 2, 3, 5, 8, 13]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_paralelogram(coords):
    x1, y1, x2, y2, x3, y3, x4, y4 = coords

    def get_length(coords):
        x1, y1, x2, y2 = coords
        result = ((x2 - x1)**2 + (y2 - y1)**2)**.5

        return result

    if get_length([x1, y1, x2, y2]) == get_length([x3, y3, x4, y4]) and get_length([x1, y1, x4, y4]) == get_length([x2, y2, x3, y3]):
        return True
    else:
        return False


print(is_paralelogram([1, 1, 4, 1, 4, 4, 1, 4]))