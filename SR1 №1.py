x1 = 3.5
x2 = -0.5
y1 = 1
y2 = 2.8
x = float(input('Введите координату x: '))
y = float(input('Введите координату y: '))
if x2 < x < x1 and y1 < y < y2:
    print('Точка принадлежит прямоугольнику')
    print('P =', ((y2 - y1) + (x1 - x2)) * 2)
    print('S =', round((y2 - y1) * (x1 - x2), 2))
if (x == x2 and y1 <= y <= y2) or (x == x1 and y1 <= y <= y2)\
        or (y == y1 and x2 <= x <= x1) or (y == y2 and x2 <= x <= x1):
    print('Точка на границе')
    c = ((x1 - x2)**2 + (y2 - y1)**2)
    d = int(c**0.5)
    print('Новые координаты (центр прямоугольника): X =', d, 'y =', d)
if ((x < x2 or x > x1) and (y == y1 or y == y2)) or ((y < y1 or y > y2) and (x == x1 or x == x2))\
        or ((x < x2 or x > x1) and (y < y1 or y > y2)):
    print('Точка не принадлежит прямоугольнику')
    a = str(input('Введите строку: '))
    b = str(input('Введите строку: '))
    if len(a) > len(b):
        if len(a) > (y2 - y1) * (x1 - x2):
            print('a > S')
        else:
            print('a < S')
    if len(b) > len(a):
        if len(b) > (y2 - y1) * (x1 - x2):
            print('b > S')
        else:
            print('b < S')
