# Write your solution here

my_list = [1,2,3,4,5]

user_index = 0

while True:

    user_index = int(input("Index: "))

    if user_index != -1:

        new_value = int(input("New value: "))

        my_list[user_index] = new_value

        print(my_list)

    else:

        break

    