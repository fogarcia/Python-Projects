# Copy here code of line function from previous exercise
def line(num, char):

    if len(char) >= 1:

        print(char[0] * num)
    
    elif char == "":

        print('*' * num)
    
    else:

        print(char * num)

def triangle(size):
    # You should call function line here with proper parameters

    count = 0

    while count <= size:

        line(count, "#" * count)

        count += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
