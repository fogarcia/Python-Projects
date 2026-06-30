# Write your solution here

my_list = []

print(f'The list is now {my_list}')

add = 0

while True:

    item = input('a(d)d, (r)emove or e(x)it: ')

    if item == 'd':

        add += 1

        my_list.append(add)

        print(f'The list is now {my_list}')
    
    elif item == 'r':

        add -= 1

        my_list.pop(-1)

        print(f'The list is now {my_list}')

    elif item == 'x':

        print('Bye!')

        break
