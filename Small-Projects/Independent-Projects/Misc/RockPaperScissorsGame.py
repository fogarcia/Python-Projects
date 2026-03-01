# Rock, Paper, Scissors Game
import random

choices = ["rock", "paper", "scissors"]

while True:
    userInput = input("Enter 'exit' to exit the game.\nEnter Rock, Paper, or Scissors:").strip().lower()
    if userInput == "exit":
        print("Thanks for playing!")
        break

    if userInput not in choices:
        print("Invalid input! Please enter Rock, Paper, or Scissors.")
        continue

    computerInput = random.choice(choices)
    print(f"Computer chose: {computerInput}")

    if userInput == computerInput:
        print("It's a tie!")
    elif (userInput == "rock" and computerInput == "scissors") or \
         (userInput == "paper" and computerInput == "rock") or \
         (userInput == "scissors" and computerInput == "paper"):
        print("You win!")
    else:
        print("You lose!")