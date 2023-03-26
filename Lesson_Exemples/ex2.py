def sum_str(*args):
    res = []
    result = 0
    for i in args:
        result += i
        res.append(result)
    return res
print(sum_str(1, 3, 5, 6, 7))
print(sum_str(3, 6, 34, 35,32,35))