filename = input("Enter filename: ")
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
    print("FILE LINES IN REVERSE ORDER")   
    for line in reversed(lines):
        print(line.rstrip())
except FileNotFoundError:
    print(f"Error: File '{filename}' not found!")