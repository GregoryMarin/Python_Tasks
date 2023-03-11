# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2
import math
max_distance = 700
fact_distance = int(input("Please write the distance: "))
print(f"You need {math.ceil(fact_distance / max_distance)} day(s) for this distance.")