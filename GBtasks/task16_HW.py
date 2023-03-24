# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

sum_numbers = int(input("Write a sum of list: "))
numbers = []
counter = 0
for i in range(sum_numbers):
    numbers.append(int(input(f"Write a {i+1} number: ")))
print(numbers)
number_find = int(input("Write a number you want to find: "))
for i in numbers:
    if i == number_find:
        counter += 1
print(f"The number '{number_find}' in the list, meets '{counter}' times.")