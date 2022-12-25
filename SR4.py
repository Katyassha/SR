print('№3')
f = input('Введите число: ')
while f != 'finish':
    if float(f) < 1:
        print('Small win')
    if 1 <= float(f) < 10:
        print('Medium win')
    if 10 <= float(f) < 20:
        print('Big win')
    f = input('Введите число: ')

###########################################
print('№1')
a = input('Введите подстроку: ')
while True:
    b = input('Введите строку: ')
    if b == 'end':
        break
    if a in b:
        print(b.replace(a, '*****'))
    if a not in b:
        print(b.replace('', ' '))
############################################
print('№2')
a = input()
while a != 'L':
    if a == 'w':
        print('Движение вперед')
    if a == 'a':
        print('Движение влево')
    if a == 's':
        print('Движение назад')
    if a == 'd':
        print('Движение вправо')
    a = input()

###############################################
print('№4')
N = int(input('Число строк: '))
A = int(input('Минимальное значение длины строки: '))
B = int(input('Максимальное значение длины строки: '))
for i in range(N):
    x = input('Введите строку: ')
    if x.isdigit():
        print('Неверный формат')
    if len(x) < A:
        print('Строка должна быть не менее', A, 'символов')
    if len(x) > B:
        print('Строка должна быть не более', B, 'символов')
    if A <= len(x) <= B:
        print('Строка удовлетворяет условиям :)')
