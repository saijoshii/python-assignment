password = input('Enter a Password: ')#Asking password from the user for the first time
confirmPassword = input('Confirm your Password: ')#Conforming password from user
if password  == "" or confirmPassword  == "" :#Condition to verify if there is some text in the password or not
    print('Password Field cannot be empty, please try again!')
else:
    if password == confirmPassword:
        print("Password Set !")
    else:
        print("Error please try again.")