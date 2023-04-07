# На вход программе подается натуральное число nn, а затем nn целых чисел.
# Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа,
# каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.

num = [int(input()) for i in range(int(input("Write a length of array: ")))]
zero = []
natur = []
not_natur = []
for i in num:
    if i < 0:
        not_natur.append(i)
    if i == 0:
        zero.append(i)
    if i > 0:
        natur.append(i)
print(*list(not_natur + zero + natur), sep="\n")
