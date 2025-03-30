# To Do List

def add_task(tasks):
    # Add a task to the list
    task = input("What task would you like to add?""\nType 'exit' to quit.\n")

    # Checks the task for empty space
    if task.strip() == "":
        print("This is not a vaild response. Please try again.")
        return

    task_num = len(tasks) + 1
    tasks.append((task_num, task))

def remove_task(tasks):

    # Displays task neatly
    for task in tasks:
        print(task)
    
    if not tasks:
        print("Your to-do list is empty. There are no tasks to remove.")
        return

    while True:

        answer = input("Which number would you like to remove?")

        if answer.lower() == "exit":
            return

        try:
            answer = int(answer)
            # Checks to see if input is vaild & removes task
            if (1 <= answer <= len(tasks)):
                del tasks[answer - 1]

                # Renumbers tasks if one is removed
                tasks[:] = [(i + 1, task[1]) for i, task in enumerate(tasks)]
                break
            else:
                print("That is not a vaild input. Please try again.")
                return
        except ValueError:
            print("That is not a vaild input. Please try again.")
            return
    
def view_tasks(tasks):
    print("Here are your current tasks:")
    print(tasks)


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

        if answer.lower() == "add task" or answer == "1":
            add_task(tasks)

        elif answer.lower() == "remove task" or answer == "2":
            remove_task(tasks)

        elif answer.lower() == "view list" or answer == "3":
            view_tasks(tasks)

        elif answer.lower() == "exit" or answer == "4":
            break
        else:
            print("That is not a valid input. Please try again.")
            continue
        print(tasks)

main()