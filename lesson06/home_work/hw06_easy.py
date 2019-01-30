class Figure(object):
    """docstring for Figure"""
    def __init__(self, coords):
        super(Figure, self).__init__()
        self._coords = coords

        # заполняем список длин сторон фигуры
        sides = []
        i = 0
        for point_A in coords:
            point_B_i = i + 1 if i + 1 < len(coords) else 0
            point_B = coords[point_B_i]
            sides.append(((point_B[0] - point_A[0])**2 + (point_B[1] - point_A[1])**2)**.5)
            i += 1
        self._sides = sides

        # разбиваем фигуру на треугольники, чтобы посчитать площадь
        triangles = []
        if len(coords) > 3:
            triangles.append((coords[0],coords[1],coords[2]))
            i = 3
            for point in coords[3:]:
                triangles.append((coords[0],coords[i-1],coords[i]))
                i += 1
        else:
            triangles.append(coords)

        square = 0
        for triangle in triangles:
            square += abs(
                (
                    (triangle[0][1] - triangle[2][1]) * (triangle[1][0] - triangle[2][0]) -
                    (triangle[0][0] - triangle[2][0]) * (triangle[1][1] - triangle[2][1])
                ) / 2)
        self._square = square


    def factory(coords):
        if len(coords) == 3:
            return Triangle(coords)
        elif len(coords) == 4:
            return EqualBarrel(coords)

    @property
    def sides(self):
        return self._sides

    @property
    def perimeter(self):
        return sum(self._sides)

    @property
    def square(self):
        return self._square

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle(Figure):
    """docstring for Triangle"""
    def __init__(self, coords):
        super(Triangle, self).__init__(coords)

    @property
    def name(self):
        return 'Triangle'

    @property
    def height(self):
        return (2 * self.square) / self._sides[0]


figure_1 = Figure.factory(((1, 1), (1, 10), (10, 1)))
print(figure_1.name)
print('площадь:', figure_1.square)
print('высота:', figure_1.height)
print('периметр:', figure_1.perimeter)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class EqualBarrel(Figure):
    """docstring for EqualBarrel"""
    def __init__(self, coords):
        super(EqualBarrel, self).__init__(coords)

    @property
    def name(self):
        return 'Equal Barrel'

    def is_EqualBarrel(self):
        return len(self._coords) == 4 and (self._sides[0] == self._sides[2] or self._sides[1] == self._sides[3])


figure_2 = Figure.factory(((0, 0), (5, 15), (10, 15), (15, 0)))
print(figure_2.name)
print(figure_2.is_EqualBarrel())
print(figure_2.sides)
print(figure_2.perimeter)
print(figure_2.square)
