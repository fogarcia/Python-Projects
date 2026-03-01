for i in range(1024):
    if i % 2 == 0:
        print("Even:", i)
    elif i < 1024:
        print("Privileged:", i)
    else:
        print("Odd:", i)