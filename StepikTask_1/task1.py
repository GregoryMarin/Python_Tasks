#  На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.
# nezabud dl-6 -> 1

s = input()
counter = 0
for i in range(10):
    counter += s.count(str(i))
print(counter)
