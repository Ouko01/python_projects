import random

def number_guessing_game():
    print("Welcome to trhe Number Guessing Game!")
    print("I have picked a number between 1 and 100. Can you guess it?")
    print("You have 3 attempts. Good luck!\n")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 3 # Total number of attempts allowed

    # Start the guessing loop
    for attempt in range(1, attempts + 1):
        try:
            # Ask the uswer for their guess
            guess = int(input(f"Attepmt {attempt}: Enter your guess: "))

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulatioins! You guessed the number {secret_number} correctly in {attempt} attempts.")
                break
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
            
            # If thi was the last attempt
            if attempt == attempts:
                print(f"Sorry, you've run out of the attempts. The correct number was {secret_number}")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    print("Game Over! Thanks for playing.")

#Run the game
if __name__ == "__main__":
    number_guessing_game()