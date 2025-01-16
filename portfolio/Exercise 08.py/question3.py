import sys

def grep(pattern, filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if pattern in line:
                    print(line, end='')  # Print matching lines without adding extra newline
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <filename>")
    else:
        grep(sys.argv[1], sys.argv[2])
