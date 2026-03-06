acceptedValues = [25, 10, 5]
amount = 50
print(f"Amount due: {amount}")

while amount > 0:
    coin = int(input("Insert a coin: "))
    change = coin - amount
    if amount > 0 and coin in acceptedValues:
        amount = amount - coin
        amount_due = amount
        if amount > 0:
            print(f"Amount due: {amount}")
    elif coin not in acceptedValues:
        print(f"Amount due: {amount}")
    else:
        break
    if amount == 0 or change >= 0:
        change = (amount_due) * -1
        print(f"Change owed: {change}")