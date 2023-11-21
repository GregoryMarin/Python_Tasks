# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True
# если число является простым и False в противном случае.

def is_prime(num):
    return len([i for i in range(1, num+1) if num % i == 0]) == 2


print(is_prime(13))
print(is_prime(1))
print(is_prime(10))
print(is_prime(17))
