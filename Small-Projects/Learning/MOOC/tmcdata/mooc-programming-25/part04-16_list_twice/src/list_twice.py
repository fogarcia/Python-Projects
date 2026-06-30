# Write your solution here

og_list = []

in_order = []

while True:

    item = int(input('New item: '))

    if item != 0:

        og_list.append(item)

        print(f'The list now: {og_list}')

        in_order.append(item)
        in_order.sort()
        print(f'The list in order: {in_order}')
    
    else:
        
        print('Bye!')

        break