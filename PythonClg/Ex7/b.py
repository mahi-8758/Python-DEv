filename = input("Enter filename: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
    
    lines = content.split('\n')
    words = content.split()
    characters = len(content)
    
    print("\n" + "=" * 50)
    print("FILE ANALYSIS")
    print("=" * 50)
    print(f"File: {filename}")
    print(f"Total Characters: {characters}")
    print(f"Total Words: {len(words)}")
    print(f"Total Lines: {len(lines)}")
    print("=" * 50)

except FileNotFoundError:
    print(f"Error: File '{filename}' not found!")