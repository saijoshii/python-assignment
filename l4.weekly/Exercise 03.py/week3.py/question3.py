password = input('Enter a Password: ')#Asking password from the user for the first time
confirmPassword = input('Confirm your Password: ') #Conforming password from user

if password == "" or confirmPassword == "":
    print('Password field cannot  be empty, please try again!')
elif 8 <= len(password) <= 12:
    if password == confirmPassword:
        print(" Password Set ")
    else:
        print('Error: Password do not match. Please try again.')
else:
    print('Enter a password that  8 to 12 characters long.')