def encrypt_message(message):
    # Remove all spaces from the message
    message_without_spaces = message.replace(" ", "")
    
    # Reverse the string without spaces
    encrypted_message = message_without_spaces[::-1]
    
    # Return the "encrypted" message
    return encrypted_message

# Test the function
message = input("Enter a message to encrypt: ")
encrypted = encrypt_message(message)
print("Encrypted message:", encrypted)
