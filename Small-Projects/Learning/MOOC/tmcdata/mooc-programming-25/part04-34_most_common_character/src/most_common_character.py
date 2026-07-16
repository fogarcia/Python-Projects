# Write your solution here

def most_common_character(string):

    count = 0

    letter = ''

    for i in string:

        num = string.count(i)

        if num > count:

            count = num

            letter = i
    
    return letter


if __name__ == '__main__':

    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
