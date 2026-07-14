# Write your solution here

def shortest(word_list):

    shortest = 'thelongandwindingroad'

    for word in word_list:

        if len(word) < len(shortest):
            shortest = word
    
    return(shortest)

if __name__ == '__main__':

    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)