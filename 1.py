#question 1
def length_conversion(value, conversion_type):
    if conversion_type == 1:  # Meters to Feet
        return value * 3.28084, "feet"
    elif conversion_type == 2:  # Kilometers to Miles
        return value * 0.621371, "miles"
    elif conversion_type == 3:  # Feet to Meters
        return value / 3.28084, "meters"
    elif conversion_type == 4:  # Miles to Kilometers
        return value / 0.621371, "kilometers"

def weight_conversion(value, conversion_type):
    if conversion_type == 1:  # Kilograms to Pounds
        return value * 2.20462, "pounds"
    elif conversion_type == 2:  # Grams to Ounces
        return value * 0.035274, "ounces"
    elif conversion_type == 3:  # Pounds to Kilograms
        return value / 2.20462, "kilograms"
    elif conversion_type == 4:  # Ounces to Grams
        return value / 0.035274, "grams"

def temperature_conversion(value, conversion_type):
    if conversion_type == 1:  # Celsius to Fahrenheit
        return (value * 9/5) + 32, "Fahrenheit"
    elif conversion_type == 2:  # Fahrenheit to Celsius
        return (value - 32) * 5/9, "Celsius"

# Define the main function which contains the unit conversion program
def main():
    # Print a welcome message for the program
    print("Unit Conversion Program")
    
    # Display the main menu for the types of conversions available
    print("1. Length Conversion")
    print("2. Weight Conversion")
    print("3. Temperature Conversion")
    
    # Ask the user to choose the type of conversion (1, 2, or 3)
    choice = int(input("Select the type of conversion (1/2/3): "))

    # Check if the user chose Length Conversion
    if choice == 1:
        print("\nLength Conversion:")  # Indicate that length conversion is selected
        # Display the options for length conversion
        print("1. Meters to Feet")
        print("2. Kilometers to Miles")
        print("3. Feet to Meters")
        print("4. Miles to Kilometers")
        
        # Ask the user to choose the specific length conversion
        conversion_choice = int(input("Select the conversion type (1/2/3/4): "))
        # Ask the user to input the value they want to convert
        value = float(input("Enter the value to convert: "))
        
        # Call the length_conversion function and get the converted value and unit
        converted_value, unit = length_conversion(value, conversion_choice)
        
        # Display the result of the conversion
        print(f"{value} converts to {converted_value:.2f} {unit}")
    
    # Check if the user chose Weight Conversion
    elif choice == 2:
        print("\nWeight Conversion:")  # Indicate that weight conversion is selected
        # Display the options for weight conversion
        print("1. Kilograms to Pounds")
        print("2. Grams to Ounces")
        print("3. Pounds to Kilograms")
        print("4. Ounces to Grams")
        
        # Ask the user to choose the specific weight conversion
        conversion_choice = int(input("Select the conversion type (1/2/3/4): "))
        # Ask the user to input the value they want to convert
        value = float(input("Enter the value to convert: "))
        
        # Call the weight_conversion function and get the converted value and unit
        converted_value, unit = weight_conversion(value, conversion_choice)
        
        # Display the result of the conversion
        print(f"{value} converts to {converted_value:.2f} {unit}")
    
    # Check if the user chose Temperature Conversion
    elif choice == 3:
        print("\nTemperature Conversion:")  # Indicate that temperature conversion is selected
        # Display the options for temperature conversion
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        
        # Ask the user to choose the specific temperature conversion
        conversion_choice = int(input("Select the conversion type (1/2): "))
        # Ask the user to input the value they want to convert
        value = float(input("Enter the value to convert: "))
        
        # Call the temperature_conversion function and get the converted value and unit
        converted_value, unit = temperature_conversion(value, conversion_choice)
        
        # Display the result of the conversion
        print(f"{value} converts to {converted_value:.2f} {unit}")
    
    # If the user entered an invalid choice
    else:
        print("Invalid choice! Please select 1, 2, or 3.")  # Display an error message

# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    main()  # Call the main function
