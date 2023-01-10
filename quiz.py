questions = ["What is the capital of France?","What is the capital of Italy?","What is the capital of Spain?","What is the capital of Germany?"]
answers = ["Paris","Rome","Madrid","Berlin"]

def ask_question_and_check_answer(question, answer):
    """Asks the user a question and returns True if their answer is correct, False otherwise."""
    user_answer = input(question)
    user_answer = user_answer.lower()
    return user_answer == answer.lower()

def run_quiz(questions, answers):
    """Runs a quiz game with the given questions and answers."""
    score = 0
    for i in range(len(questions)):
        question = questions[i]
        answer = answers[i]
        
        if ask_question_and_check_answer(question, answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", answer)
    return score

def pretty_print_results(score, total):
    """Prints the final results of the quiz game."""
    print("You scored", score, "out of", total)
    if score == total:
        print("Congratulations! You got a perfect score!")
    elif score / total >= 0.75:
        print("Congratulations! You passed with a high score.")
    else:
        print("Unfortunately, you did not pass. Better luck next time.")

# Run the quiz and print the results
score = run_quiz(questions, answers)
pretty_print_results(score, len(questions))