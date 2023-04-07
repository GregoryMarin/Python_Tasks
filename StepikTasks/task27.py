# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.
# Напишите программу, которая выводит инициалы человека.

s = input().split()
st = []
for i in s:
    for j in i:
        if j == i[0]:
            st.append(j)
print('.'.join(st), end='.')

# Marin Grigorii Vasilievich