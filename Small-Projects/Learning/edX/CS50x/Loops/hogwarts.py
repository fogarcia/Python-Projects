# List of dictionaries :o!

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=": ")

# students = {
#             "Hermione": "Gryffindor", 
#             "Harry": "Gryffindor", 
#             "Ron": "Gryffindor", 
#             "Draco": "Slytherin"
# }

# for student in students:
#     print(student, students[student], sep=": ")

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# students = ["Hermione", "Harry", "Ron", "Draco"]

# print(students[0])
# print(students[1])
# print(students[2])

# Using 'student' as a variable name to represent each student in the list 
# 'students' instead of '_' to make it more descriptive and easier to understand.

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])
