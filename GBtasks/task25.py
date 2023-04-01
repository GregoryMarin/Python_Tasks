# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже
# встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
#
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
#
# Для решения данной задачи используйте функцию .split()

# s = ('a a a b c a a d c d d').split()
# dict = {}
# for i in s:
#     if i not in dict:
#         dict[i] = 0
#         print(i, end=' ')
#     elif i in dict:
#         dict[i] += 1
#         print(f"{i}_{dict[i]}", end=' ')

l = 'a a a b c a a d c d d'
l = l.replace(' ','')
print(list)
i, n, st = 0, len(l),''

while i<n:
    if l[:i].count(l[i])==0 : st += f'{l[i]}'
    else : st += f'{l[i]}_{l[:i]}.count{l[i]}'
    i += 1
print(st)