def decrypt_message(encrypted_message, interval):
    # Initialize an empty list to hold the decrypted characters
    decrypted_message = []
    
    # Iterate over the encrypted message, taking every 'interval' character
    for i in range(0, len(encrypted_message), interval):
        decrypted_message.append(encrypted_message[i])  # Append the character at the current interval
    
    # Join the list into a single string to form the decrypted message
    return ''.join(decrypted_message)

if __name__ == "__main__":
    # Example usage
    encrypted = "sxyexyneycxyhxyexyexysxye"  
    interval = 5  # This should match the interval used during encryption
    
    decrypted = decrypt_message(encrypted, interval)
    
    print(f"Encrypted Message: {encrypted}")
    print(f"Interval Used: {interval}")
    print(f"Decrypted Message: {decrypted}")
