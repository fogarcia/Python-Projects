# Quiz

# This is a simple quiz program
def quiz():
    score = 0
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "What is the capital of Spain?": "Madrid"
    }
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            score += 1
    print("Your score is:", score)
if __name__ == "__main__":
    quiz()
    print("Thank you for taking the quiz!")
