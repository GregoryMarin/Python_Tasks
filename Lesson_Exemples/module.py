def max_number(*args):
    max_num = args[0]
    for i in args:
        if (i+1) > max_num:
            max_num = i
    return max_num