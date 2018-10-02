# coding : utf-8

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5

equation = equation.replace(' ', '')
k = float(equation[equation.find('=') + 1:equation.find('x')])
b = float(equation[equation.find('x') + 1:])

y = k*x + b
print(y)
