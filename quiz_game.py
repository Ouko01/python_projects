import json
import random
import time

# Function to load questions from a file
def load_questions(filename):
    try:
        with open (filename, encoding='utf-8') as file:
            return json. load(file)
    except FileNotFoundError:
        print("Error: File not found!")
        return []

def run_quiz(questions, time_limit=10):
    print("Welcome to the Quiz Game!")
    print("You have a time limit of 10 seconds for each question.")
    print("Good luck!\n")

    score = 0 # Initialize score

    # Shuffle questions
    random.shuffle(questions)

    # Loop through the questions
    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: {question['question']}")
        for option in question['options']:
            print(option)
        
        # Start the timer
        start_time = time.time()
        user_answer = None

        # Check for time limit
        while time.time() - start_time < time_limit:
            user_answer = input("Your answer (A, B, C, or D): ").upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input! Please enter A, B, C, or D")

        # Time check
        if not user_answer or time.time() - start_time >= time_limit:
            print("Time's up! Moving to the next question.\n")
            continue # Skip to the next question

        # Check if the answeer is correct
        if user_answer == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.\n")
    
    # Display the final score
    print("Quiz Complete!")
    print(f"Your final score is: {score} out of {len(questions)}")

# Run the quiz
if __name__ == "__main__":
    # Load questions from the JSON file
    questions = load_questions("quiz_questions.json")

    if questions:
        run_quiz(questions, time_limit=10) # Set a 10-second tier per question
    else:
        print("No question available. Please check your file.")