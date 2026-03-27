menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
for item in menu:
    try:
        item = input("Item: ").title()
        price = menu.get(item)
        total += price
        print(f'Total: ${"%0.2f" % total}')
    except TypeError:
        continue
    except EOFError:
        print(f'\nTotal: ${"%0.2f" % total}')
        break