# Write your solution here

def longest_series_of_neighbours(list):

    neighbours = []

    for i in list:

        if list.index(i):

            ...


if __name__ == '__main__':

    #neightbors 1,2 : 7,6 : 5,6 : 3,4

    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
