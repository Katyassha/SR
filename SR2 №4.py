import math
s = 0
b = int(input('Введите количество значений: '))
for i in range(1, b + 1):
    n = float(input())
    s += (math.cos(math.radians(n + 1)) / (2 * n))
print('Сумма =', round(s, 3))
