def total(a=5, *numbers, **phonebook):
    print('a', a)

# Проход по всем элементам кортежа
    for single_item in numbers:
        print("single_item", single_item)
# Проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)
print(total(10, 1, 2, 3, Jack=1123, Jhon=2231, Inge=1560))