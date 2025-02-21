# Calculator app 
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"


def calculator():
    print("Welcome to the Calculator App!")
    print("Select an operation: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        try:
            choice = int(input("\nEnter you=r choice (1/2/3/4/5): "))
            if choice == 5:
                print("Exiting the calculator. Goodbye!")
                break

            if choice in (1, 2, 3, 4):
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == 1:
                    print(f"The result is:  {add(num1, num2)}")
                elif choice == 2:
                    print(f"The result is:  {sub(num1, num2)}")
                elif choice == 3:
                    print(f"The result is:  {mul(num1, num2)}")
                elif choice == 4:
                    print(f"The result is:  {div(num1, num2)}")
            else:
                print("Invalid choice. Please choose a valid operation.")    
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
# Run the calculator
calculator()
