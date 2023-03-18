# На вход программе подается натуральное число n \ge 2n≥2, а затем nn целых чисел.
# Напишите программу, которая создает из указанных чисел список,
# состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).

# size = int(input("WRITE A SIZE OF ARRAY: "))
# s = []
# for i in range(size):
#     if i < size - 1:
#         i += 1
#         s.append(i + (i+1))
# print(s)

size = int(input("WRITE A SIZE OF ARRAY: "))
s = []
s2 = []
for i in range(size):
    s.append(int(input()))
    i += 1
for i in range(size):
    s2[i] = (sum(s[i], s[i])
    i += 1
print(s2)