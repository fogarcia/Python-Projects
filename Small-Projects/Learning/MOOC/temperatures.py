# Write your solution here

fahrenheit = int(input("Please type in a temperature(F): "))

celsius = (fahrenheit - 32) * 5/9

if celsius < 0:
    print(f'{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius')
    print("Brr! It's cold in here!")
else:
    print(f'{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius')