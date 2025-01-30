# To Do List

def main():
    tasks = []
    menu ="""
    1. Add Task
    2. Remove Task
    3. View List
    4. Exit
    """
    print(menu)

    while True:
        answer = input("What would you like to do?")

        if answer == "Add Task" or answer == "1":
            task = input("What task would you like to add?")
            tasks.append(task)
        elif answer == "2":
            remove = input("Which task would you like to remove?")
        elif answer == "3":
            print(tasks)
        elif answer == "4":
            break
        else:
            answer = input("That is not a valid input. Please try again.")
        print(tasks)

main()