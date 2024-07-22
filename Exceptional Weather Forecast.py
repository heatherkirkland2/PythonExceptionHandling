'''
Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process. What happens if they type out "thirty" instead of doing 30?

Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 

Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.
'''

def convert_temperature(fahrenheit):
    try:
        # Convert the Fahrenheit temperature to Celsius
        celsius = (fahrenheit - 32) * 5/9
    except TypeError:
        # Handle the case where the input is not a number
        print("The temperature entered is not a valid number. Please enter a numeric value.")
    else:
        # Print the converted temperature in a user-friendly format
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    finally:
        # Thank the user for using the weather forecast application
        print("Thank you for using the weather forecast application.")

# Start by asking the user to enter the temperature in Fahrenheit
user_input = input("Please enter the temperature in Fahrenheit: ")

try:
    # Attempt to convert the user input to a float
    fahrenheit_temperature = float(user_input)
    convert_temperature(fahrenheit_temperature)
except ValueError:
    # Handle the case where the input cannot be converted to a float
    print("The temperature entered is not a valid number. Please enter a numeric value.")
