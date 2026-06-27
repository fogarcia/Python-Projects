# Write your solution here

print("Please type in integer numbers. Type in 0 to finish.")

count = 0
posCount = 0
negCount = 0
sumONum = 0
meanONum = 0
number = 0

while True:

    number = int(input("Number: "))

    if number == 0:
        break
    elif number > 0:
        posCount += 1
    elif number < 0:
        negCount +=1
    else:
        continue
    
    count += 1
    sumONum += number
    

meanONum = sumONum/count

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sumONum}")
print(f"The mean of the numbers is {meanONum}")
print(f"Positive numbers {posCount}")
print(f"Negative numbers {negCount}")
