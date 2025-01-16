def letters_in_either(word1, word2):
    return sorted(set(word1) | set(word2))  # Union of both sets

def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))  # Intersection of both sets

def letters_in_one_but_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2))  # Symmetric difference of both sets

# Test the functions
word1 = input("Enter  first word: ")
word2 = input("Enter  second word: ")

print("Letters in either word:", letters_in_either(word1, word2))
print("Letters in both words:", letters_in_both(word1, word2))
print("Letters in one but not both:", letters_in_one_but_not_both(word1, word2))