camelCase = input("camelCase:")

snake_case = []

for letter in camelCase:
    current_index = camelCase.index(letter)
    if letter == letter.upper() and current_index > 0:
        letter = "_" + letter.lower()
        snake_case.append(letter)
    elif letter == letter.upper() and current_index < 0:
        letter = "_" + letter.lower()
        snake_case.append(letter)
    else:
        letter = letter.lower()
        snake_case.append(letter)

print(f"snake_case: {''.join(snake_case)}")
