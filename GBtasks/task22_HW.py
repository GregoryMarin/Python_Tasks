# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

def numbers(n, m):
    n_num = []
    m_num = []
    sorted_nums = []
    for i in range(n):
        n_num.append(int(input("Write a 'n' values: ")))
    print("Very good! Continue!")

    for i in range(m):
        m_num.append(int(input("Write a 'm' values: ")))
    sorted_nums = sorted(list(set(n_num) & set(m_num)))

    print(f'n_num = {n_num}')
    print(f'm_num = {m_num}')
    print(sorted_nums)

numbers(5, 5)