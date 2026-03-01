# Multiple ways to print "Meow" three times

# i = 3

# while i != 0:
#     print("Meow")
#     i = i - 1

# for _ in range(3):
#     print("Meow")

# Less readable, but more concise
# print("Meow\n" * 3, end="")

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("Meow")

def main():
    number = get_number()

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()