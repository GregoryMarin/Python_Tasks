# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

def fillarray(n):
    array = []
    for i in range(n):
        array.append(int(input(f"Write a number {i+1}: ")))
    return array


def find_dif(n, m, r):
    for i in n:
        if i not in m:
            r.append(i)
    return r


count1 = int(input("Write an array1 length: "))
array1 = fillarray(count1)

count2 = int(input("Write an array2 length: "))
array2 = fillarray(count2)

new_array = []
print(array1)
print(array2)
print(find_dif(array1, array2, new_array))