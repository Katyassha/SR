a = input('Введите строку: ')
b = input('Введите подстроку: ')
if b in a:
    print('Подстрока «', b, '» есть в строке «', a, '»', sep='')
    x = (3.14 + len(a)) / len(b)
    print('X=', round(x, 6))
elif len(a) % 2 == 0 and len(a) % 5 == 0:
    print('Подстрока «', b, '» отсутствует в строке «', a, '»', sep='')
    print('Длина строки четна и кратна 5')
    print(a + b, len(a + b),  sep='\n')
elif len(a) % 2 != 0 and len(a) % 3 == 0:
    print('Длина строки нечетна и кратна 3')
    print('Введите 3 строки:')
    c = input()
    d = input()
    e = input()
    print('Строка', max(c, d, e), '– наибольшая по длине')
