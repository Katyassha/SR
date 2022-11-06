import math
a = float(input('Левая граница: '))
b = float(input('Правая граница: '))
h = float(input('Задайте величину шага: '))
while a <= b:
    y = round(((math.exp(a) - (math.exp(a)) ** -1) / 2) ** 3, 3)
    print('x = ', a, '; y = ', y, sep='')
    a = round(a + h, 3)
