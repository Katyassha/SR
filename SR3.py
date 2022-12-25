import math
print('№1')


def function(a1, b1, h1):
    mas = []
    while a1 <= b1:
        y1 = round(((math.exp(a1) - math.exp(-a1)) / 2) ** 3, 3)
        mas.append(y1)
        a1 = round(a1 + h1, 3)
    return mas


a = float(input('Левая граница: '))
b = float(input('Правая граница: '))
h = float(input('Задайте величину шага: '))
y = function(a, b, h)
print(y)
#######################################################################
print('№2')


def _chislo_(a):
    mas = list()
    if float(a) >= 0 or int(a) >= 0:
        mas.append('Положительное')
    else:
        mas.append('Отрицательное')
    if '.' in a:
        mas.append('дробное')
    else:
        mas.append('целое')
    b = 0
    for i in a:
        if i != '.':
            b += 1
    mas.append(b)
    c = 0
    for i in reversed(a):
        if '.' in a:
            if i != '.':
                c += 1
        if i == '.':
            break
    mas.append(c)
    return mas


n = input('Введите число: ')
_chislo_(n)
print(_chislo_(n))
#######################################################################
print('№3')

my_list = ['Магазин', 'Часы', 'Рыбалка', 'Уксус', 'Полотенце', 'Микроволновка', 'Вода', 'Столешница', 'Смысл']
my_file = open('YourList.txt', 'w+')
for i in range(len(my_list)):
    my_file.write(my_list[i] + "\n")
my_file.close()


def find_str(string):
    with open('BabyFile.txt', 'r') as file:
        for line in file:
            if string in line:
                print(line)


string = input('Введите строку: ')
find_str(string)
