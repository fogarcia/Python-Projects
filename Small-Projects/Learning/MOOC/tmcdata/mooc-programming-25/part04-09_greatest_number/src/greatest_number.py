# Write your solution here
def greatest_number(num, num1, num2):
    if num >= num1 and num >= num2:
        return num
    elif num1 >= num and num1 >= num2:
        return num1
    elif num2 >= num and num2 >= num1:
        return num2
    else:
        return num
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)