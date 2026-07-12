# Write your solution here

def sum_of_positives(list):

    posList = []

    for i in list:

        if i > 0:

            posList.append(i)
        
        else:

            continue
    print(posList)

    result = 0

    for i in posList:

        result += i
        
    return result




if __name__ == "__main__":

    my_list = [1,-2,3,-4,5]
    result = sum_of_positives(my_list)
    print("The result is", result)