toDoList = []

while True:
    
    task = input("Enter task:")

    toDoList.append(task)

    print(toDoList)

    if task == "q" or task == "Q":
        break