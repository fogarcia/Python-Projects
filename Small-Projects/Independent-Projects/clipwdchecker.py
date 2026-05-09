pwd = input("What is your password?")

# This program checks the strength of a password based on its length, 
# the number of special characters, numbers, and uppercase letters it 
# contains. The password is rated as weak, moderate, or strong based on 
# the total score calculated from these criteria.

# A count is kept for each of the criteria, and a score is calculated based on the following rules:
# - Length of 12 or more characters adds 1 point to the score
# - More than 1 special character adds 1 point to the score
# - More than 1 number adds 1 point to the score
# - More than 1 uppercase letter adds 1 point to the score
score = 0
length = 0
special_count = 0
num_count = 0
upper_count = 0

# TODO: Tidy up the code, make it more efficient, and add comments to explain what each part does


for char in pwd:
    length += 1

for char in pwd:
    if not char.isalnum():
        special_count += 1

for char in pwd:
    if char.isnumeric():
        num_count += 1

for char in pwd:
    if char.isupper():
        upper_count += 1

if length >= 12:
    score += 1
if special_count > 1:
    score += 1
if num_count > 1:
    score += 1
if upper_count > 1:
    score += 1

print(f"Special: {special_count}, Number: {num_count}, Upper: {upper_count}")

print(f"Length: {length}")
print(f"Score: {score}")

if score <= 1:
    print("Rating: Weak")
elif score <= 3:
    print("Rating: Moderate")
elif score >= 4:
    print("Rating: Strong")