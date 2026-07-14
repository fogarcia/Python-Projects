# Write your solution here

def length_of_longest(list):

    longest = []

    for i in list:

        if len(i) != longest:

            longest.append(len(i))
    
    return(max(longest))
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)