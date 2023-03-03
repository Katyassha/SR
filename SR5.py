import math
import statistics
print('№1')


def func(*args):
    print('Среднее арифметическое:', statistics.mean(args))
    print('Дисперсия:', round(statistics.pvariance(args), 3))
    print('Среднеквадратическое отклонение:', round(math.sqrt(statistics.pvariance(args)), 3))
    print('Коэффициент вариации:', round(math.sqrt(statistics.pvariance(args)) / statistics.mean(args), 3))


n = int(input('Введите желаемое количество значений: '))
myList = []
for _ in range(n):
    myList.append(float(input()))
func(*myList)
####################################################################################
print('№2')


def lists(*args):
    list_of_str = []
    list_of_num = []
    list_of_bool = []
    list_of_other = []
    for i in range(len(args)):
        a = str(args[i])
        b = args[i]
        if type(b) == bool:
            list_of_bool.append(b)
        elif a.isalpha():
            list_of_str.append(b)
        elif a.replace('.', '').isdigit():
            if '.' in a:
                list_of_num.append(float(a))
            else:
                list_of_num.append(int(a))
        else:
            list_of_other.append(b)
    print('list_of_str', list_of_str)
    print('list_of_num', list_of_num)
    print('list_of_bool', list_of_bool)
    print('list_of_other', list_of_other)


lists(False, 2.3, (1, 3), True, 'Heellloooo', 22, ['яблоко', 'банан'])
####################################################################################
print('№3')


def myDictFunc(arg, **kwargs):
    for i in range(len(kwargs)):
        if arg == list(kwargs)[i]:
            print('{}: {}'.format(arg, kwargs.get(arg)))
        a = list(kwargs.values())[i]
        if arg == list(a)[0]:
            print(a)


myDict = {'1': {'DEBUG': 'Tracemod'}, '2': {'ERROR': 'Null pointer exception'}, '3': {'INFO': 'startGameAllert'},
          '4': {'DEBUG': 'sendAllert'}, '5': {'ERROR': 'No valid JSON'}, 'ERROR': 'Error'}
myDictFunc('ERROR', **myDict)

