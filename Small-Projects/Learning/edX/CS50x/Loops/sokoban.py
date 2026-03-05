def main():
    history = []
    
    while True:
        action = input("Action: ")

        if action == "Undo":
            if not history:
                print("There is nothing to undo.")
            else:
                undone = history.pop()
                print(f"Undone {undone}")
        elif action == "restart" or action == "Restart":
            history.clear()
            print("The game has restarted.")
        else:
            history.append(action)
        print(history)

main()