import sys

def main():
    # takes args except the script name
    args = sys.argv[1:]  
    if not args:
        print("Oops! No arguments given.")
        return
    
    # Sorting by length to get the shortest one
    args.sort(key=len)
    print(f"Shortest one: {args[0]}")  # Just showing the first shortest

if __name__ == "__main__":
    main()
