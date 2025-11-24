string = input("Enter a string: ")
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("CHARACTER COUNT")
print(f"String: {string}")
print(f"Character Count: {char_count}")
for char, count in char_count.items():
    print(f"'{char}': {count}")
