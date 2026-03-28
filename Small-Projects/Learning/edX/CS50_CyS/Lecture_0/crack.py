# 10,000 possible combinations of 4 digits
# from string import digits

# for i in digits:
#     for j in digits:
#         for k in digits:
#             for l in digits:
#                 print(i + j + k + l)


# 7,000,000 possible combinations of 4 letters (upper and lowercase)
# from string import ascii_letters

# for i in ascii_letters:
#     for j in ascii_letters:
#         for k in ascii_letters:
#             for l in ascii_letters:
#                 print(i + j + k + l)

# 70,000,000 possible combinations of 4 characters (upper and lowercase letters, digits, and punctuation)
from string import ascii_letters, digits, punctuation

for i in ascii_letters + digits + punctuation:
    for j in ascii_letters + digits + punctuation:
        for k in ascii_letters + digits + punctuation:
            for l in ascii_letters + digits + punctuation:
                print(i + j + k + l)