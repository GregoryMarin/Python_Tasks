"""Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель
за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями
статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период,
в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам
в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день.
Температуры – целые числа и лежат в диапазоне от –50 до 50

Input: 6 -> -20 30 -40 50 10 -10
Output: 2
"""

# a=int(input("Введите а: "))
# first=0
# second=1
#
# if a==0:
#     print(1)
# elif a==1:
#     print(2)
#
# count=2
# while second<a:
#     buffer=first+second
#     first=second
#     second=buffer
#     count+=1
# if second==a:
#     print(count)
# else:
#     print(-1)

number = int(input("Введите число: "))
f1 = f2 = 1
n = 3 # число больше 1
while number > f2 :
    f1, f2 = f2, f1 + f2
    n += 1
print(n if number == f2 else '-1')