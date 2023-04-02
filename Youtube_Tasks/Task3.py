# s = input()
# ans = ''
# anscnt = 0
# for i in range(len(s)):
#     nowcnt = 0
#     for j in range(len(s)):
#         if s[j] == s[i]:
#             nowcnt += 1
#     if nowcnt > anscnt:
#         ans = s[i]
#         anscnt = nowcnt
# print(ans)
# ========================================
s = input()
ans = ''
anscnt = 0
dct = {}
for now in s:
    if now not in dct:
        dct[now] = 0
    dct[now] += 1
for key in dct:
    if dct[key] < anscnt:
        anscnt = dct[key]
        ans = key
print(dct)