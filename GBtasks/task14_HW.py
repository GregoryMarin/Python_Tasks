# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input("Введите число: "))
result = 0
array_num = []
for i in range(number):
    result = 2**(i)
    if result <= number:
        array_num.append(result)
        i += 1
print(array_num)

# Эту задачку сам решил, она вроде не сложная