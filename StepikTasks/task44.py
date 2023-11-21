# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
#
# def some_program(numb):
#     if is_even(numb):
#         print("Это число четное")
#     else:
#         print("Это число не четное")
#
#
# some_program(int(input("Введите число: ")))

def is_invalid(model):
    if model != 100 and model != 200 and model != 300:
        return True
    else:
        return False


model = int(input())
while is_invalid(model):
    print('Допустимыми номерами моделей являются 100, 200 и 300.')
    model = int(input())
