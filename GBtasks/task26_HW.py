# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


# def degree(a, b):
#     if b == 1:
#         return a
#     return (degree(a) * pow(degree(a), b-1))
# print(degree(3, 5))

def power(a, b):
    if (b == 1):
        return (a)
    return (a * power(a, b - 1))
a = int(input("Введите число: "))
b = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(a, b))




