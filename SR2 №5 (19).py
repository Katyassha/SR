n = int(input('Размер матрицы (i = j): '))
for i in range(1, n + 1):
    k = ''
    for j in range(1, n + 1):
        if i != j:
            k += '0 '
        # Для того, чтобы границы матрицы были ровными можно добавить это условие
        # Но при нем перед полученными значениями получаются небольшие пробелы
        # elif n > 4 and i == j > (n - 4):
        #    k += ' ' + str(2 * n - 2 * (i - 1)) + ' '
        elif i == j:
            k += str(2 * n - 2 * (i - 1)) + ' '
    print(k)
