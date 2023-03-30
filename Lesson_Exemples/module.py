def max_number(*args):
    max_num = args[0]
    for i in args:
        if (i+1) > max_num:
            max_num = i
    return max_num

def string(args):
    while True:
        args = input("Write a word: ")
        if args == 'exit':
            print("Excellent!")
            break
        if len(args) < 3:
            print("Too small word!")
            continue
        print("The string is a normal length)")