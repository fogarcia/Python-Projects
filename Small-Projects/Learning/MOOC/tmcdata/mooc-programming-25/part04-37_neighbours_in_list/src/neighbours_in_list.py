# Write your solution here

def longest_series_of_neighbours(list):

    current_streak = 1

    max_streak = 1

    for i in range(1, len(list)):

        if list[i] - list[i-1] == 1 or list[i-1] - list[i] == 1:

            current_streak += 1

            if current_streak > max_streak:

                max_streak = current_streak
        else:

            current_streak = 1
            
    return max_streak
if __name__ == '__main__':

    #neightbors 1,2 : 7,6 : 5,6 : 3,4

    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
