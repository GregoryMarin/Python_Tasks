# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
#
# Output: 1 3 3 3 1

# def count(num):
#     my_min = min(num)
#     my_max = max(num)
#     for i in range(len(num)):
#         if num[i] == my_max:
#             num[i] = my_min
#     return num
#
# number = [1, 4, 6, 5, 2, 6]
# print(count(number))

def min_max_serch(input_list):
    return min(input_list), max(input_list)


def min_max_replace(start_list, copy=True):
    if copy:
        start_list = start_list.copy()
    min_el, max_el = min_max_serch(start_list)
    while max_el in start_list:
        max_index = start_list.index(max_el)
        start_list[max_index] = min_el
    return start_list



start_list = [1, 4, 3, 7, 7]
print(min_max_replace(start_list))