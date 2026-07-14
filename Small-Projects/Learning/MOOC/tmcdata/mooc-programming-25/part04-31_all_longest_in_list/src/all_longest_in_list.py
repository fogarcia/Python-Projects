# Write your solution here

def all_the_longest(list):
    tmp = ''

    longest_name = []

    for name in list:

        if len(name) > len(tmp):

            tmp = name
    
    longest_name.append(tmp)

    for name in list:

        if len(tmp) == len(name) and tmp != name:

            longest_name.append(name)
    
    return longest_name



if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']