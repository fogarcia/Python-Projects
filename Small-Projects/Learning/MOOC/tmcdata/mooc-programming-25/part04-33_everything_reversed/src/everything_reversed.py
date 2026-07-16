# Write your solution here

def everything_reversed(list):

    reversed_list = list[::-1]

    another_list = []

    for i in reversed_list:

        another_list.append(i[::-1])
    
    return another_list

if __name__ == '__main__':
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)