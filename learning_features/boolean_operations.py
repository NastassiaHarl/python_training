# '''Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17.
#  Напишите программу, определяющую, является ли введённое число красивым.
#  Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.'''
#
# number = int(input('Add number: '))
#
# if (number > 999 and number < 10000) and (number % 7 == 0 or number % 17 == 0):
#     print('YES')
# else:
#     print('NO')

# '''Напишите программу, которая принимает три положительных числа и определяет,
# существует ли невырожденный треугольник с такими сторонами.'''
#
# number = int(input('Add number: '))
# number1 = int(input('Add number: '))
# number2 = int(input('Add number: '))
#
# if (number + number1 > number2) and (number + number2 > number1) and (number1 + number2 > number):
#     print('YES')
# else:
#     print('NO')

# '''Напишите программу, которая определяет, является ли год с данным номером високосным.
# Если год является високосным, то выведите «YES», иначе выведите «NO».
# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400'''
#
# number = int(input('Add number: '))
#
# if (number % 4 == 0 and number % 100 != 0) or number % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# '''Даны две различные клетки шахматной доски. Напишите программу,
# которая определяет, может ли ладья попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца
# и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести «YES», если из первой клетки ходом ладьи можно попасть во вторую,
# или «NO» в противном случае.'''

# number = int(input('Add number: '))
# number1 = int(input('Add number: '))
# number2 = int(input('Add number: '))
# number3 = int(input('Add number: '))
#
# if (number != number2) and (number1 == number3):
#     print('YES')
# elif (number == number2) and (number1 != number3):
#     print('YES')
# else:
#     print('NO')

'''Даны две различные клетки шахматной доски.
Напишите программу,которая определяет,
может ли король попасть с первой клетки на вторую одним ходом.
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки,
потом для второй клетки. Программа должна вывести «YES»,
если из первой клетки ходом короля можно попасть во вторую,
или «NO» в противном случае.'''

a = int(input('Add number: '))
b = int(input('Add number: '))
c = int(input('Add number: '))
d = int(input('Add number: '))

if (c >= (a - 1)) and (c <= (a + 1)):
    print('YES')
elif (d >= (b - 1)) and (d <= (b + 1)):
    print('YES')
else:
    print('NO')

# '''a - 1 <= c <= a + 1,
#
# b - 1 <= d <= b + 1'''''