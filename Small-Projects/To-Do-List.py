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

        # Allows user to choose from a menu of options

        answer = input("What would you like to do?")

        if answer == "Add Task" or answer == "1":
            task = input("What task would you like to add?")
            task_num = len(tasks) + 1
            tasks.append((task_num, task))
        elif answer == "Remove Task" or answer == "2":

            # Displays task neatly
            for task in tasks:
                print(task)

            if not tasks:
                print("Your to-do list is empty. There are no tasks to remove.")
                continue

            number = int(input("Which number would you like to remove?"))

            # Checks to see if input is vaild & removes task
            if (1 <= number <= len(tasks)):
                del tasks[number - 1]

                # Renumbers tasks if one is removed
                tasks = [(i + 1, task[1]) for i, task in enumerate(tasks)]
            else:
                print("That is not a vaild input. Please try again.")
                continue

        elif answer == "View List" or answer == "3":
            print("Here are your current tasks:")
            print(tasks)
        elif answer == "Exit" or answer == "4":
            break
        else:
            print("That is not a valid input. Please try again.")
            continue
        print(tasks)

main()