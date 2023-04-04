# На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит
# k-ую букву из введенных строк на одной строке без пробелов.

n = int(input())
array = []
new_arr = []
for i in range(n):
    array.append(input())
k = int(input())
for i in array:
    for j in range(len(i)):
        if j == k - 1:
            new_arr.append(i[j])
print("".join(new_arr))