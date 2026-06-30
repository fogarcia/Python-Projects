# Write your solution here

items = int(input('How many items: '))

count = 0

item_list = []

while count < items:

    if count < items:

        item = input(f'Item {count + 1}: ')

        item = int(item)

        item_list.append(item)
    
    count += 1

print(item_list)