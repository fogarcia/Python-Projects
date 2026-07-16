# Write your solution here

def no_shouting(list):

    lower_list = []

    for i in list:

        if i.isupper():

            continue
        
        else:

            lower_list.append(i)

            continue
    
    return lower_list

            


if __name__ == '__main__':

    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)