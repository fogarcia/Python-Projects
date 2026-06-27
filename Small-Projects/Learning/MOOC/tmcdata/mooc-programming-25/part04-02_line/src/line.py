# Write your solution here
def line(num, char):

    if len(char) >= 1:

        print(char[0] * num)
    
    elif char == "":

        print('*' * num)
    
    else:

        print(char * num)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(3, "")