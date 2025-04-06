# List Overlap

import random


a = []
b = []

for i in range(random.randint(1, 10)):
    a.append(random.randint(1, 10))
print(a)

for i in range(random.randint(1, 10)):
    b.append(random.randint(1, 10))
print(b)

inCommon = []

for i in a:
    if i in b:
        if i not in inCommon:
            inCommon.append(i)

print(inCommon)