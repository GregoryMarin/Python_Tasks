# Задача 4:
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
import math
summ = int(input("Общее кол-во журавликов: "))
if summ > 5 and summ % 2 == 0:
    k = (summ / 3) + (summ / 3)
    print(f"Петя = {round(k / 4)}, Катя = {round(k)}, Сережа = {round(k / 4)}")
else:
    print("Число должно быть больше 5 и должно быть четным!")