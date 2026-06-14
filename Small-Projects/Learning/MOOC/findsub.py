# Write your solution here

word = input('Please type in a word: ')
character = input('Please type in a character: ')

index = word.find(character)

count = index

while count != index + 3:
    count += 1

if len(word[index:count]) < 3:
    print()
else:
    print(word[index:count])