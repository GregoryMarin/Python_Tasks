num = [1, 2, 3, 5, 8, 15, 23, 38]


def find_natural(n):
    numbs = []
    for i in n:
        if i % 2 == 0:
            numbs.append((i, i**2))
    return numbs


print(find_natural(num))
