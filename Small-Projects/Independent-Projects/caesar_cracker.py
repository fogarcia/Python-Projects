caesar_string = "hwtxxnslymjwzgnhtswlvhsgdv"

shift = 22

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

decrypted = []

for letter in caesar_string:
    new_shift = alphabet.index(letter) - shift

    new_letter = alphabet[new_shift]

    decrypted.append(new_letter)

print("".join(decrypted))
