#################################################################################
print('№3')
import math
a = float(input('Левая граница: '))
b = float(input('Правая граница: '))
h = float(input('Задайте величину шага: '))
while a <= b:
    y = round(((math.exp(a) - math.exp(-a)) / 2) ** 3, 3)
    print('x = ', a, '; y = ', y, sep='')
    a = round(a + h, 3)
###############################################################################################
print('№4')
import math
s = 0
b = int(input('Введите количество значений: '))
for i in range(1, b + 1):
    n = float(input())
    s += (math.cos(math.radians(n + 1)) / (2 * n))
print('Сумма =', round(s, 3))
################################################################################################
print('№5')
n = int(input('Размер матрицы (i = j): '))
s = 0
for i in range(1, n + 1):
    k = ''
    for j in range(1, n + 1):
        if i != j:
            k += '0 '
        elif i == j:
            k += str(2 * n - 2 * (i - 1)) + ' '
            s += 2 * n - 2 * (i - 1)
    print(k)
print(s)
