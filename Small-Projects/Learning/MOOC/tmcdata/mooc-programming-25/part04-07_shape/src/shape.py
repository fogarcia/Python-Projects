# Copy here code of line function from previous exercise and use it in your solution
def line(num, char):

    if len(char) >= 1:

        print(char[0] * num)
    
    elif char == "":

        print('*' * num)
    
    else:

        print(char * num)

def shape(num, char, num2, char2):

    count = 0

    while count <= num:

        line(count, char * count)

        count += 1

    count = 1

    while count <= num2:

        line(num, char2 * count)

        count += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")