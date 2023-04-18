# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

PATH_FILE = r'Phonebook.txt'


def console_menu():
    pass


def read_file():
    with open(PATH_FILE, 'r') as f:
        for line in f:
            print(line.strip())


def write_file():
    with open(PATH_FILE, 'a') as f:
        f.writelines('\n' + input())


def find_file():
    find_info = input()
    with open(PATH_FILE, 'r') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)


def change_file():
    find_info = input()
    new_info = input()
    with open(PATH_FILE, 'r+') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                lst = (line.strip()).split(' ')
                print(lst)

def main():
    while True:
        i = input("What you want to do? (Write: 'r', or 'f', or 'a'): ")
        if i == 'r':
            read_file()
        if i == 'a':
            write_file()
        if i == 'f':
            find_file()
        if i == 'exit':
            break
        print("!!! For exit - write: 'exit'")




if __name__ == '__main__':
    main()
