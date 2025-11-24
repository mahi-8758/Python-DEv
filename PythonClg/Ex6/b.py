filename = input("Enter filename: ")
with open(filename, 'r') as file:
    content = file.read().lower()
char_freq = {}
for char in content:
    if char.isalpha():
        char_freq[char] = char_freq.get(char, 0) + 1
print("CHARACTER FREQUENCY ANALYSIS")
print(f"File: {filename}")
print(f"Total characters: {len(char_freq)}")
print(f"Frequency: {char_freq}")

python_chars = {'d', 'e', 'f', 'i', 'n', 't', 'r', 'u', 'o'}
c_chars = {'i', 'n', 't', 'r', 'e', 'f', 'o', 'r', 'w', 'h', 'l'}

python_score = sum(1 for char in python_chars if char in char_freq)
c_score = sum(1 for char in c_chars if char in char_freq)

print(f"\nPython Score: {python_score}")
print(f"C Score: {c_score}")

if python_score > c_score:
    print("File Type: Python Program")
elif c_score > python_score:
    print("File Type: C Program")
else:
    print("File Type: Text File")
