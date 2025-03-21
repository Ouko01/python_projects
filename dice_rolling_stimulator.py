import random

def roll_dice():
    # Generate a random number between 1 and 6
    return random.randint(1, 6)

def dice_simulator():
    print("Welcom to the Dice Rolling Simulator!")
    while True:
        # Ask the user if they eant to roll the dice
        roll = input("Roll the dice? (yes/no)").lowercase()
        if roll == "yes":
            # Roll the dice and display the result
            result = roll_dice()
            print(f"You rolled a {result}!")
        elif roll == "no":
            # Exit the loop if the user doesn't want to roll the dice
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Run the dice simulator
dice_simulator()