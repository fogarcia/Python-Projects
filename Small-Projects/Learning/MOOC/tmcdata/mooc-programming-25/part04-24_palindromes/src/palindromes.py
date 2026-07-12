# Write your solution here
def palindromes(string):

    list = []

    backwardsList = []

    count = 0

    backwards = -1

    for i in string:

        list.append(i)

    while count < len(string):

        backwardsList.append(list[backwards])

        count += 1

        backwards -= 1

    if backwardsList == list:
        return True
    else:
        return False
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
string = input('Please type in a palindrome: ')

while True:
    
    if palindromes(string) == True:
        print(f'{string} is a palindrome!')
        break
    else:
        print("that wasn't a palindrome")
        string = input('Please type in a palindrome: ')