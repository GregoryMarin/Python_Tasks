# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

#-----1-----------
# number = int(input("Write a number: "))
# r = number % 10
# g = number % 100 // 10
# b = number // 100
# res = r + g + b
# print(f"Summ of ({b}, {g}, {r}) = {res};")

#-------2---------
num = int(input("Write a number: "))
print(f"Summ of elements your number = {(num % 10) + (num % 100 // 10) + (num // 100)} ")
