num = int(input("Enter a number: "))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

less = []
for i in a:
    if i < num:
        less.append(i)
print(less)

less = [i for i in a if i < num]

temp = []
for i in a:
    if i < 5:
        temp.append(i)
print(temp)

temp = [i for i in a if i < 5]
print(temp)