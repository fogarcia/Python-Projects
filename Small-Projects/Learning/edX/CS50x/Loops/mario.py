def main():
    print_square(3)

def print_square(size):
    # For each row in the square
    for i in range(size):
        print_row(size)
        # print("#" * size, end="")
        # For each brick in row
        # for j in range(size):

        #     # Print brick
        #     print("#", end="")
        
        # Print new line at end of row
        print()

def print_row(width):
    print("#" * width, end="")

# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

# def main():
#     print_column(3)

# def print_column(height):
#     # for _ in range(height):
#     #     print("#")
#     print("#\n" * height, end="")

main()

# for _ in range(3):
#     print("#")

# print("#")
# print("#")
# print("#")