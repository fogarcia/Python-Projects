# Write your solution here

def list_sum(list_a, list_b):

    sum_list = []

    index = 0

    while index < len(list_a):

        sum_list.append(list_a[index] + list_b[index])

        index += 1
    
    return(sum_list)

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))