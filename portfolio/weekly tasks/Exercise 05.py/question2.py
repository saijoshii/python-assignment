import sys

def main(): #This function prints the number of arguments passed to the script.
    num_arg = len(sys.argv) - 1 #calculate number of arguments
    print(f"Number of arguments provided: {num_arg}")

if __name__ == "__main__":
    main()
