# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while
# Простое решение
number = int(input("Введите число: "))
res = 1
while number > 1:
    res *= number
    number -= 1
print(res)

# Второе решение
number = int(input("Введите число: "))
res = 1
while number > 1:
    res *= number
    number -= 1
print(res)