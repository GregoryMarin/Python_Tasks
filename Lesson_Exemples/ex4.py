# def math(op, x, y):
#     print(op(x,y))
# math(lambda a,b: a+b, 5, 45)

# def numbers(*args):
#     for i in range(len(args)):
#         print(lambda args[0], result[] : result = args[0] * args[0])
# =======================================================================
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = []
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)
# =======================================================================
# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)
# ========================================================================
data = '2 23 42 5 36 6 57 35 75'
data = list(map(int, data.split()))
print(data)