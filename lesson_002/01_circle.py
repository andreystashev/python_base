#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()

print(round(42 ** 2 * 3.1415926,4))

# TODO Да, вот так через переменные и оставьте, а строку выше удалите
pi = 3.1415926
print(round(radius ** 2 * pi,4))



# Далее, пусть есть координаты точки
point_1 = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False

# TODO Не нужно делать словарь, используйте сразу point_1 и point_2. Раз центр находится в точке 0,0, то в расчетах ее
#  можно вообще не использовать
sites = {
'point_1': (23, 34),
'point_2': (0,0),
}
distances = dict ()
point_1 = sites ['point_1']
centre = sites ['point_2']
point_1_centre = ((point_1[0] - centre[0]) ** 2 + (point_1[1] - centre[1]) ** 2) ** .5

distances ['point'] = point_1_centre
a = 42  # TODO У нас уже есть переменная radius
b = point_1_centre  # TODO А зачем делать еще одну переменную b?
print (a>b)



# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.

sites = {
'centre': (0, 0),
'point_2': (30,30),
}
distances = dict ()
centre = sites ['centre']
point_2 = sites ['point_2']
centre_point_2 = ((centre[0] - point_2[0]) ** 2 + (centre[1] - point_2[1]) ** 2) ** .5

distances ['point'] = centre_point_2

a = 42
b = centre_point_2
print (a>b)

# Пример вывода на консоль:
#
# 77777.7777
# False
# False
