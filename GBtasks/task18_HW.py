# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

count_numbers = int(input("Write a sum of numbers: "))
list_num = []
for i in range(count_numbers):
    list_num.append(int(input(f"The number {i+1}: ")))
print(list_num)
numberX = int(input("Write a number you want: "))
counter_list = []
for i in list_num:
    counter_list.append(i - numberX)
minimum = min(counter_list)
print(counter_list)
for i in counter_list:
    if i == minimum:
        print(f"The {list_num[i]} is nearest to number {numberX}")