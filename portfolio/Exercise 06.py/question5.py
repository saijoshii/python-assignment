import random
import string

def encrypt_message(message): # Generate a random interval between 2 and 20
    interval = random.randint(2, 20)
    
    # Create a list to hold the encrypted characters
    encrypted_message = []
    
    # Iterate through the message and insert random letters
    for char in message:
        encrypted_message.append(char)  # Add the original character
        
        # Insert random letters after each character
        for _ in range(interval - 1):  # Fill (interval - 1) times
            random_letter = random.choice(string.ascii_lowercase)
            encrypted_message.append(random_letter)
    
    # Join the list into a single string to form the encrypted message
    return ''.join(encrypted_message), interval

if __name__ == "__main__":
    original_message = "send cheese"
    encrypted, interval = encrypt_message(original_message)
    
    print(f"Original Message: {original_message}")
    print(f"Random Interval: {interval}")
    print(f"Encrypted Message: {encrypted}")
