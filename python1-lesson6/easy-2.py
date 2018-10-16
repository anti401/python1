# coding : utf-8

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Trapezium:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        # сразу считаем длины сторон
        self.AB = self.len_side(A, B)
        self.BC = self.len_side(B, C)
        self.CD = self.len_side(C, D)
        self.AD = self.len_side(A, D)
        # и диагоналей
        self.AC = self.len_side(A, C)
        self.BD = self.len_side(B, D)

    def len_side(self, P1, P2):
        """Длина стороны"""
        return ((P1.x - P2.x) ** 2 + (P1.y - P2.y) ** 2) ** 0.5

    def is_isosceles(self):
        """Проверка на равнобедренность"""
        return self.AC == self.BD

    def perimeter(self):
        """Периметр"""
        return self.AB + self.BC + self.CD + self.AD

    def area(self):
        """Площадь"""
        return (self.BC + self.AD) / 4 * (4 * self.AB ** 2 - (self.BC - self.AD) ** 2) ** 0.5


sample = Trapezium(Point(1, 1), Point(2, 5), Point(5, 5), Point(6, 1))

if sample.is_isosceles():
    print('AB = {}'.format(sample.AB))
    print('BC = {}'.format(sample.BC))
    print('CD = {}'.format(sample.CD))
    print('AD = {}'.format(sample.AD))
    print('Трапеция равнобедренная!')
    print('Периметр = {}'.format(sample.perimeter()))
    print('Площадь = {}'.format(sample.area()))
else:
    print('AB = {}'.format(sample.AB))
    print('BC = {}'.format(sample.BC))
    print('CD = {}'.format(sample.CD))
    print('AD = {}'.format(sample.AD))
    print('Это не равнобедренная трапеция.')
