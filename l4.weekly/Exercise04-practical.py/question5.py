def celcius_to_Fahrenheit():
    number = float(input('Enter Temperature : '))
    fahrenheit = (number * 9/5) + 32
    print(fahrenheit)
    
    
def fahrenheit_to_Celcius():
    number = float(input('Enter Temperature : '))
    celcius = (number - 32) * 5/9
    print(celcius)
    
    
print("Press 1 to Convert Celcius to Fahrenheit \n")
print("Press 2 to Convert Fahrenheit to Celcius \n")
choice = input("Enter your choice: ")

if choice == '1':
    celcius_to_Fahrenheit()
else:
    fahrenheit_to_Celcius()