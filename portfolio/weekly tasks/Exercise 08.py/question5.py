import sys
import string

def load_dictionary(dictionary_file):
    with open(dictionary_file, 'r') as file:
        return {word.strip().lower() for word in file}

def spell_check(file_name, dictionary_file):
    valid_words = load_dictionary(dictionary_file)
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                words = line.lower().translate(str.maketrans('', '', string.punctuation)).split()
                unknown_words = [word for word in words if word not in valid_words]
                for word in unknown_words:
                    print(word)
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

if len(sys.argv) > 2:
    file_name = sys.argv[1]
    dictionary_file = sys.argv[2]
    spell_check(file_name, dictionary_file)
else:
    print("Please provide a file name and a dictionary file as command-line arguments.")