vowels = ['a', 'i', 'e', 'o', 'u', 'A', 'I', 'E', 'O', 'U']

tweet = input("Input: ")
letters = []
for letter in tweet:
    if letter not in vowels:
        letters.append(letter)

print(f"Output: {''.join(letters)}")