def checkLetter():
    word = input('Enter a word: ')
    length = len(word)
    uppercaseLetter = 0 
    lowercaseLetter = 0 
    for char in word:
        if char.isupper():
            uppercaseLetter += 1
        else:
            lowercaseLetter += 1
    print("Total length", length),
    print("Total uppercase letter are ",uppercaseLetter)
    print("Total lowercase letter are", lowercaseLetter)
    
checkLetter()