# coding : utf-8

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        # сразу считаем длины сторон
        self.AB = self.len_side(A, B)
        self.BC = self.len_side(B, C)
        self.AC = self.len_side(A, C)

    def len_side(self, P1, P2):
        """Длина стороны"""
        return ((P1.x - P2.x) ** 2 + (P1.y - P2.y) ** 2) ** 0.5

    def perimeter(self):
        """Периметр"""
        return self.AB + self.BC + self.AC

    def area(self):
        """Площадь по формуле Герона"""
        p = self.perimeter() / 2
        return (p * (p - self.AB) * (p - self.BC) * (p - self.AC)) ** 0.5

    def heights(self):
        """Высоты треугольника"""
        s = self.area()
        return tuple(map(lambda side: 2 * s / side, [self.AB, self.BC, self.AC]))


sample = Triangle(Point(1, 1), Point(3, 5), Point(5, 1))
print('Периметр = {}'.format(sample.perimeter()))
print('Площадь = {}'.format(sample.area()))
print('Высоты = {}'.format(sample.heights()))
