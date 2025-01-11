# Define a list of given common passwords
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:  # Loop until a valid password is chosen
    password = input('Enter a Password: ')
    confirmPassword = input('Confirm your Password: ')

    # Check if any of the password fields are empty
    if password == "" or confirmPassword == "":
        print('Password field cannot be empty, try again!')
    # Check if the password length is between 8 and 12 characters
    elif 8 <= len(password) <= 12:
        # Check if the password is one of the common passwords
        if password.lower() in BAD_PASSWORDS:
            print(' password is too common, please choose a different one.')
        elif password == confirmPassword:
            print('Password Set !')
            break  # Exit the loop if password is valid and matches
        else:
            print('Error: Passwords do not match. please try again.')
    else:
        print('Enter a password that is 8 to 12 characters long.')