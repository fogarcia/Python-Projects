# Write your solution here
def same_chars(string, num, num1):
    if num >= len(string) or num1 >= len(string):
        return False
    elif string[num] == string[num1]:
        return True
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))