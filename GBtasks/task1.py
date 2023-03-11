# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт,
# которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

import math
# a = int(input('Введите количество учеников в 1 классе '))
# b = int(input('Введите количество учеников в 2 классе '))
# c = int(input('Введите количество учеников в 3 классе '))
# print(math.ceil((a+b+c)/2))

# Дано натуральное число.
# Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4,
# но не кратен 100, а также если он кратен 400.
# Input: 2016
# Output: YES

year = int(input("Введите год "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("YES")
else:
    print("NO")

