# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def fibo(num):
#     if num == 0 or num == 1:
#         return 1
#     return fibo(num-1) + fibo(num-2)
#
# number = int(input("Write a number: "))
# print(fibo(number))

def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(7))