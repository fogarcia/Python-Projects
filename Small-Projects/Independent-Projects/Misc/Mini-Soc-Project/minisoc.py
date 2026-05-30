log_file = input("Enter the log file name: ")

terms = ["ERROR", "WARNING", "DENIED", "unauthorized"]

with open(log_file, 'r') as file:
    for i in file:
        for term in terms:
            if term in i:
                print(i.strip())