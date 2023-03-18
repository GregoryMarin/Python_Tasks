'''Задача 10:
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же
стороной. Выведите минимальное количество монет, которые нужно перевернуть'''
# eagle = 1
# tails = 0
amount = int(input("Write number of coins: "))
coins = []
count_one = 0
count_zero = 0
for i in range(amount):
    coins.append(int(input("Write a side of coin (eagle = 1; tails = 0): ")))
    if coins[i] == 1 or coins[i] == 0:
        if coins[i] == 1:
            count_one += 1
        else:
            count_zero += 1
    else:
        print('Incorrect value! There is must be only "1" or "0" ')
        break
if count_zero < count_one:
    print(count_zero)
else:
    print(count_one)

# Не знаю как сдалать так, чтобы после ошибки, код с 21-24 строки не выполнялся