
size = int(input("Write a size of array: "))
i = 0
userList = []
while i < size:
    string = 'Enter element #' + str(i+1) + ': '
    userList.append((input(string)))
    userList.append(int(input("Write a value: ")))
    i += 1
print(userList)


