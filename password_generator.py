import random
import string
import json

def generate_password(length):
    # Define the character sets to use
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + symbols

    # Ensure length is at least 4 for a strong password.
    if length < 4:
        print("Password length should be at least 4 characters for a strong password.")
        return None

    # Randomly generate a password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def save_password(password, filename='passwords.json'):
    # Try to load existing data
    try:
        with open(filename, 'r') as file:
            passwords = json.load(file) # Read JSON data
            if not isinstance(passwords, dict):
                passwords = {}
    except (FileNotFoundError, json.JSONDecodeError): # Handle file not found or invalid JSON
        print("No existing passwords found or file is corrupted. Creating a new file.")
        passwords = {}

    # Save the new password with a label
    label = input("Enter a label for this password(e.g., Email, Banking): ")
    passwords[label] = password

    # Write back to the file
    with open(filename, 'w') as file:
        json.dump(passwords, file, indent=4)
    print(f"Password saved to {filename} under the label '{label}'.")

# Ask the user for the password length
try:
    password_length = int(input("Enter the desired password length: "))
    # Generate and print the password
    generated_password = generate_password(password_length)
    if generated_password:
        print("Generated Password:", generated_password)
        save_choice = input("Do you want to save this password? (y/n): ").lower()
        if save_choice == 'y':
            save_password(generated_password)
except ValueError:
    print("Invalid input. Please enter a valid integer for the password length.")