"""Unit converter: length, temperature, weight"""

def length_conversion(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "feet": 3.28084,
        "inches": 39.3701
    }
    if from_unit not in length_units or to_unit not in length_units:
        raise ValueError("Invalid unit. Supported units are: meters, kilometers, miles, feet, inches.")
    return value * length_units[to_unit] / length_units[from_unit]

def temperature_convertion(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value # Same unit
    
def weight_conveter(value, from_unit, to_unit):
    weight_units = {
        "kilograms": 1,
        "pounds": 2.20462,
        "grams": 1000
    }
    if from_unit not in weight_units or to_unit not in weight_units:
        raise ValueError("Invalid unit. Supported units are: kilograms, pounds, grams.")
    return value * weight_units[to_unit] / weight_units[from_unit]

def unit_conveter():
    print("Welcome to the Unit Converter!")
    while True:
        print("Choose a category:")
        print("1. Length\n2. Temperature\n3. Weight\nType 'e' to exit.")
        choice = input("Enter your choice (1-3) or 'e': ").strip().lower()
        if choice == "e":
            print("Thank you for using the Unit Converter. Goodbye!")
            break
        try:
            if choice not in ('1', '2', '3'):
                raise ValueError("Invalid choice. Please choose a number between 1 and 3.")
        except ValueError as e:
            print(f"Error: {e}. Please try again!")
            return
        
        try:
            if choice == 1:
                print("Length Units: meters, kilometers, miles, feet, inches")
                from_unit = input("Convert from: ").lower()
                to_unit = input("Convert to: ").lower()
                value = float(input(f"Enter value in {from_unit}: "))
                result = length_conversion(value, from_unit, to_unit)

            elif choice == 2:
                print("Temperature Units: Celsius, Fahrenheit, Kelvin")
                from_unit = input("Convert from: ").capitalize()
                to_unit = input("Convert to: ").capitalize()
                value = float(input(f"Enter value in {from_unit}: "))
                result = temperature_convertion(value, from_unit, to_unit)

            elif choice == 3:
                print("Weight Units: kilograms, pounds, grams")
                from_unit = input("Convert from: ").lower()
                to_unit = input("Convert to: ").lower()
                value = float(input(f"Enter value in ({from_unit}: "))
                result = weight_conveter(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result:.2f} {to_unit}")
            print(f"{value} {from_unit} = {result:.2f} {to_unit}")
        except ValueError as e:
            print(f"Error: {e}. Please check your input and try again!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    unit_conveter()
