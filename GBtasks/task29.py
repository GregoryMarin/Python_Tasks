# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем
# (число 0 не входит в последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог
# до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью
# товарищи обратились к Вам, студентам.
#
# Примечание: Программные коды на следующих слайдах

numbers = int(input("Write a number: "))
max_num = numbers
while numbers != 0:
    numbers = int(input("Write a number: "))
    if numbers > max_num:
        max_num = numbers
print(f'Max number you entered => {max_num}')
