# При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое
# значение.
# На вход программе подается натуральное число nn, а затем nn различных натуральных чисел.
# Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся
# числа каждое на отдельной строке, не меняя их порядок.

n = int(input())
arr = []
for u in range(n):
    arr.append(int(input()))
m = min(arr)
n = max(arr)
for i in arr:
    if i == m or i == n:
        arr.remove(m)
        arr.remove(n)
print(*arr, sep="\n")