grocery_list = []
count = {}
sorted_count = {}
while True:
    try:
        item = input("")
        grocery_list.append(item)
    except EOFError:
        for i in grocery_list:
            if not i in count:
                count[i] = 1
            else:
                count[i] += 1
        for key, value in count.items():
            sorted_count = dict(sorted(count.items()))
        for key, value in sorted_count.items():
            print(value, key.upper())
        break