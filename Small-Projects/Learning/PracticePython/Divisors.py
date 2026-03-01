# Divisors

num = int(input("Enter a number: "))

x = range(1, 1001)

for i in x:
    if i % num == 0:
        print(i)

# listRange = list(range(1, num+1))

# divisorList = []

# for number in listRange:
#     if num % number == 0:
#         divisorList.append(num)

# print(divisorList)