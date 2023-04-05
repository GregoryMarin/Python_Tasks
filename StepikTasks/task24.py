# На вход программе подается натуральное число nn, а затем nn строк. Напишите программу, которая выводит только
# уникальные строки, в том же порядке, в котором они были введены.

arr = []
for i in range(int(input("Write a length of array: "))):
    s = input(f"{i+1}: ").lower()
    if s not in arr:
        arr.append(s)
print(arr)