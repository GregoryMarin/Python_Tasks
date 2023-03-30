
def guess_number(arg):
    number = arg
    running = True

    while running:
        n = int(input("Write a number: "))
        if n == number:
            running = False
        elif n > number:
            print("The number slightly less)")
        else:
            print("The number a little more!")
    else:
        print("Cycle while is finished")