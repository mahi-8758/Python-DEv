def dups(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates
print("FIND DUPLICATES IN LIST")


numbers = [1, 2, 3, 2, 4, 5, 3, 6, 7, 2, 8]
strings = ["apple", "banana", "apple", "cherry", "banana", "date"]
print(f"\nList 1: {numbers}")
print(f"Duplicates: {dups(numbers)}")

print(f"\nList 2: {strings}")
print(f"Duplicates: {dups(strings)}")