# coding : utf-8

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def middle(A, B):
    # середина отрезка
    return (A[0] + B[0]) / 2, (A[1] + B[1]) / 2


def equals(A, B):
    # совпадение точек
    return A[0] == B[0] and A[1] == B[1]


points = [1, 1], [2, 4], [4, 1], [5, 4]

# если совпадают середины диагоналей - параллелограмм
if equals(middle(points[0], points[1]), middle(points[2], points[3])):
    print('Это параллелограмм!')
elif equals(middle(points[0], points[2]), middle(points[1], points[3])):
    print('Это параллелограмм!')
elif equals(middle(points[0], points[3]), middle(points[2], points[1])):
    print('Это параллелограмм!')
else:
    print('Это не параллелограмм.')
