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

# '''Даны две различные клетки шахматной доски.
# Напишите программу,которая определяет,
# может ли король попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки,
# потом для второй клетки. Программа должна вывести «YES»,
# если из первой клетки ходом короля можно попасть во вторую,
# или «NO» в противном случае.'''
#
# a = int(input('Add number: '))
# b = int(input('Add number: '))
# c = int(input('Add number: '))
# d = int(input('Add number: '))
#
# if (c >= (a - 1)) and (c <= (a + 1)):
#     print('YES')
# elif (d >= (b - 1)) and (d <= (b + 1)):
#     print('YES')
# else:
#     print('NO')

# n = int(input('Зума'))
# k = int(input('Флэша'))
#
# if n > k:
#     print('NO')
# elif n < k:
#     print('YES')
# else:
#     print("Don't know")

# Формат входных данных
# На вход программе подаются три числа – длины сторон существующего треугольника.
#
# Формат выходных данных
# Программа должна вывести на экран текст – вид треугольника
# («Равносторонний», «Равнобедренный» или «Разносторонний»).

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a == b and b == c:
#     print('Равносторонний')
# elif a == b and b != c:
#     print('Равнобедренный')
# elif a == c and b != c:
#     print('Равнобедренный')
# elif a != b and b == c:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')
#
# Формат входных данных
# На вход программе подаётся три различных целых числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести среднее число.
#
# Примечание. Средним называется число, которое будет вторым,
# если три числа отсортировать в порядке возрастания.

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a < b and b < c:
#     print(b)
# elif c < b and b < a:
#     print(b)
# elif b < a and a < c:
#     print(a)
# elif c < a and a < b:
#     print(a)
# elif a < c and c < b:
#     print(c)
# else:
#     print(c)

# a = int(input())
#
# if a == 2:
#     print('28')
# elif a == 4 or a == 6 or a == 9 or a == 11:
#     print('30')
# else:
#     print('31')


# Известен вес боксера-любителя (целое число).
# Известно, что вес таков, что боксер может быть отнесён к одной из трех весовых категорий:
#
# Легкий вес – до 60 кг;
# Первый полусредний вес – до 64 кг;
# Полусредний вес – до 69 кг.
# Напишите программу, определяющую, в какой категории будет выступать данный боксер.

# a = int(input())
#
# if a < 60:
#     print('Легкий вес')
# elif a >= 60 and a < 64:
#     print('Первый полусредний')
# elif a >= 64 and a < 69:
#     print('Полусредний вес')

# Самописный калькулятор 🌶️
# Напишите программу, которая считывает с клавиатуры два целых числа и строку.
# Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /),
# то выведите результат применения этой операции к введённым ранее числам,
# в противном случае выведите «Неверная операция».
# Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!»

# a = int(input())
# b = int(input())
# c = input()
#
# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '*':
#     print(a * b)
# elif c == '/':
#         if  b == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(a / b)
# else:
#     print('Неверная операция')

# Красный, синий и желтый называются основными цветами,
# потому что их нельзя получить путем смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:
#
# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания.
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый»,
# то программа должна вывести сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета, который получится в результате.

# a = input()
# b = input()
#
# if a == 'красный' and b == 'красный':
#     print('красный')
# elif a == 'красный' and b == 'синий' or b == 'красный' and a == 'синий':
#     print('фиолетовый')
# elif a == 'красный' and b == 'желтый' or b == 'красный' and a == 'желтый':
#     print('оранжевый')
# elif a == 'синий' and b == 'синий':
#     print('синий')
# elif a == 'синий' and b == 'желтый' or b == 'синий' and a == 'желтый':
#     print('зеленый')
# elif a == 'желтый' and b == 'желтый':
#     print('желтый')
# else:
#     print('ошибка цвета')

# На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов:
#
# карман 0 зеленый;
# для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный;
# для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.
#
# Напишите программу, которая считывает номер кармана и показывает,
# является ли этот карман зеленым, красным или черным.
# Программа должна вывести сообщение об ошибке, если пользователь вводит число,
# которое лежит вне диапазона от 0 до 36.


# a = int(input())
#
# if a == 0:
#     print('зеленый')
# elif a >= 1 and a <= 10:
#     if a % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif a >= 11 and a <= 18:
#     if a % 2 == 0:
#         print('красный')
#     else:
#         print('черный')
# elif a >= 19 and a <= 28:
#     if a % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif a >= 29 and a <= 36:
#     if a % 2 == 0:
#         print('красный')
#     else:
#         print('черный')
# else:
#     print('ошибка ввода')

# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
#
# if a2 > b1 or b2 < a1:
#     print('пустое множество')
# else:
#     if a2 == b1 or b2 == a1:
#         print(b1, a1)
#     elif a1 <= a2 < b1 < b2:
#         print(b1, a2)
#     elif a2 <= a1 < b2 < b1:
#         print(b2, a1)
#     elif a1 <= a2 < b2 <= b1:
#         print(b2, a2)
#     elif a2 <= a1 < b1 <= b2:
#         print(b1, a1)
#     elif a2 == a1 and b1 == b2:
#         print(b1, a1)

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a2 > b1 or b2 < a1:
    print('пустое множество')
else:
    if a1 < a2 and b1 > b2:
        print(a2, b2)
    elif b2 > b1 and a2 > a1 and a2 != b1:
        print(a2, b1)
    elif a1 > a2 and b2 < a1 and b2 != a1:
        print(a1, b2)
    elif a1 > a2 and b1 < b2 and a2 != b1 and b2 != a1:
        print(a1, b1)
    elif b2 > b1 and a2 == b1:
        print(b1)
    elif a2 < a1 and b2 == a1:
        print(a1)
    elif a1 == a2 and b1 == b2:
        print(a1, b2)
    elif a1 == a2 and b1 < b2:
        print(a1, b1)
    elif b1 == b2 and a1 > a2:
        print(a1, b1)
    elif a1 == a2 and b2 < b1:
        print(b1, b2)
    elif b1 == b2 and a2 > a1:
        print(a2, b1)