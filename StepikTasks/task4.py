# На вход программе подается строка текста.
# Напишите программу, которая выводит на экран символ, который появляется наиболее часто.
# aaaabbc -> a
print('Write a string: ')
s = input()
counter = 0
a = ''
for i in s:
    if s.count(i) >= counter:
        counter = s.count(i)
        a = i
print(a)
