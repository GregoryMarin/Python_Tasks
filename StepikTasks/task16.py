# На вход программе подается натуральное число n >= 2, а затем n целых чисел. Напишите программу,
# которая создает из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).

n = int(input("Write a number: "))
cort = []
cort_res = []
for i in range(n):
    cort.append(int(input()))
print(cort)
for i in range(len(cort)-1):
    cort_res.append(cort[i] + cort[i+1])
print(cort_res)
