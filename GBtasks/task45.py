def sum_div(num):
    sum_ = 0
    for i in range(1, num):
        if num % i == 0:
            sum_ += i
    return sum_


k = 300
for num_1 in range(2, k + 1):
    num_2 = sum_div(num_1)
    sum_num_2 = sum_div(num_2)
    if (num_1 < num_2) and (sum_num_2 == num_1):
        print(num_1, num_2)