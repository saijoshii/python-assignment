def convert_celsius_to_fahrenheit(celsius):#Converts Celsius temperature to Fahrenheit.
    
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Get user input
input_temp = input("Enter temperature in Celsius (e.g., 25C): ")

# Check if input ends with 'C' or 'c'
if input_temp[-1].upper() == 'C':
    try:
        # Extract the numeric part of the input (removing 'C') and convert it to float
        celsius = float(input_temp[:-1])
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        # Display the result with Fahrenheit value followed by 'F', rounded to 2 decimal places
        print(f"{fahrenheit:.2f}F")
    except ValueError:
        print("Invalid input. Please enter a valid number followed by 'C'.")
else:
    print("Invalid input. Please enter a temperature followed by 'C'.")
