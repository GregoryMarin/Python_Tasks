list_str = [int(i) for i in input().split()]
list_str.sort()
print(*list_str)
list_str.sort(reverse=True)
print(*list_str)


