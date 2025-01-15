import sys

def nl_command(filename):
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}\t{line}", end='')  # Print line number and line content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nl_command.py <filename>")
    else:
        nl_command(sys.argv[1])
