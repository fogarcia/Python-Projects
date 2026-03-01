hello = input("Go ahead:").split(",")

print(hello)


if hello.isdigit():
    print("NUMBER")
elif hello.isdigit() & isinstance(hello, str):
    print("NUMEBER AND DIGIT")
else:
    for char in hello:
        print(char)