# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя ни одной из операций деления: ни деления с плавающей точкой /, ни целочисленного деления //
# и взятия остатка %
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b, count = 179, 37, 0
b1 = b
while a > b1 - 1:
    # TODO подкорректировал условие, проверил, так вычисляется верно при условии что числа берутся положительные и целые
    count += 1
    b1 = b1 + b
else:
    print('Целочисленное деление', a, 'на', b, 'дает', count)
