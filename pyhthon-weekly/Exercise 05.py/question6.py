import sys
import os

def create_backup(file_name):
    backup_name = file_name + ".bak"
    with open(file_name, 'rb') as original_file:
        with open(backup_name, 'wb') as backup_file:
            backup_file.write(original_file.read())
    print(f"Backup created: {backup_name}")

if len(sys.argv) > 1:
    file_name = sys.argv[1]
    if os.path.isfile(file_name):
        create_backup(file_name)
    else:
        print(f"The file {file_name} does not exist.")
else:
    print("Please provide the name of the file as a command-line argument.")