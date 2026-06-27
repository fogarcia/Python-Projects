# Write your solution here

num = int(input("Number 1: "))
num2 = int(input("Number 2: "))

operation = input("Operation: ")

if operation == "add":
    print(f'{num} + {num2} =', num + num2)
elif operation == "subtract":
    print(f'{num} - {num2} =', num - num2)
elif operation == "multiply":
    print(f'{num} * {num2} =', num * num2)
elif operation == "divide":
    print(f'{num} / {num2} =', num / num2)