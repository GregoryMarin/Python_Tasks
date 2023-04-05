# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая для каждого
# введенного числа x выводит значение функции f(x) = x^2 + 2x + 1f(x)=x каждое на отдельной строке.

n = int(input())
arr = []
for u in range(n):
    arr.append(int(input()))
print(*arr, sep="\n")
print()
for i in range(n):
    arr[i] = (arr[i]**2) + (2 * arr[i]) + 1
print(*arr, sep="\n")