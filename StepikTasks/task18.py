# def total(initial=5, *numbers, extra_number):
#     count = initial
#     for number in numbers:
#         count += number
#         count += extra_number
#         print(count)
# total(10, 1, 2, 3, extra_number=50)
# total(10, 1, 2, 3)
# # Вызовет ошибку, поскольку мы не указали значение # аргумента по умолчанию для 'extra_number'.

def printMax(x, y):
    '''Выводит максимальное из двух чисел.
    Оба значения должны быть целыми числами.'''
    x = int(x) # конвертируем в целые, если возможно y = int(y)
    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')

printMax(23, 45)
print(printMax.__doc__)
