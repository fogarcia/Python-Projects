def main():
    words = get_words("address.txt")
    lowercase_words = [word.lower() for word in words if len(word) > 4]


    counts = {word: words.count(word) for word in lowercase_words}
    # for word in lowercase_words:
    #     if word in counts:
    #         counts[word] += 1
    #     else:
    #         counts[word] = 1
    
    save_counts(counts)


def get_words(filename):
    with open(filename) as file:
        return file.read().split()

def save_counts(counts):
    with open("address.txt", "w") as file:
        for word, count in counts.items():
            file.write(f"{word}: {count}\n")

main()