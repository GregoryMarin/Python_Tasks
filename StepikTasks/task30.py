# На вход программе подается строка текста, содержащая целые числа. Напишите программу, которая по заданным числам
# строит столбчатую диаграмму.

lst = input().split()
for i in range(len(lst)):
    lst[i] = int(lst[i])
print(lst)
for num in lst:
    print('*' * num)