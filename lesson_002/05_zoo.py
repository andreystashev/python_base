#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль

zoo.insert (1,'bear')
print (zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo.extend(birds)

print (zoo)

# уберите слона
#  и выведите список на консоль

#removed_item = zoo.pop(zoo.index('elephant'))

zoo.remove('elephant')
print (zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

a=zoo.index ('lion')+1
b=zoo.index ('lark')+1
print (a, '- лев', ';', b, '- жаворонок' )

# зачет!




