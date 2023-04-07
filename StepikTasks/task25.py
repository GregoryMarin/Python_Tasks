# На вход программе подается натуральное число nn, затем nn строк, затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.

l1 = [input(f"{x}: ") for x in range(int(input("Write a count of array: ")))]
l2 = [input(f"{x}: ") for x in range(int(input("Words, you want to find: ")))]
result = []
for i in l1:
    counter = 0
    for j in l2:
        if j.lower() in i.lower():
            counter += 1
            if counter == len(l2):
                result.append(i)
print(*result, sep="\n")
