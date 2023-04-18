def print_digit_sum(num):
    s = 0
    for i in num:
        s += int(i)
    print(s)

n = input()
print_digit_sum(n)
