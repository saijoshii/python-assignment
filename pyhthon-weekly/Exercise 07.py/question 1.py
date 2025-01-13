def get_unique_letters(input_str):
    # Create a set to store unique letters 
    unique_chars = set(input_str)
    
    # Sort the set and return it as a list
    sorted_chars = sorted(unique_chars)
    
    return sorted_chars

# Test the function
user_input = input("Enter a string: ")
result = get_unique_letters(user_input)
print("Sorted unique letters:", result)
