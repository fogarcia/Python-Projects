# Write your solution here
def first_word(sentence):
    index = 0

    while index < len(sentence):

        if sentence[index] == " ":
            return sentence[0:index]
        index+= 1

def second_word(sentence):
    index = 0

    while index < len(sentence):

        if sentence[index] == " ":

            first_space = index

            index = first_space + 1

            while index < len(sentence):

                if sentence[index] == " ":

                    return sentence[first_space + 1:index]
                
                index += 1
        index += 1
    
    return sentence[first_space + 1:]

def last_word(sentence):
    index = 0

    while index < len(sentence):

        if sentence[index] == " ":
            return sentence[index + 1:]
        index-= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word("first second"))
    print(last_word(sentence))