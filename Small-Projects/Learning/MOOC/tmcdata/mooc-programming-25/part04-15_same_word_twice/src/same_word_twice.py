# Write your solution here

word_list = []

count = 0

while True:

    word = input('Word: ')

    if word not in word_list:

        word_list.append(word)
    
    else:

        break

    count += 1

print(f'You typed in {count} different words')