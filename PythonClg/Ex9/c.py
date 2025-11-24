def unique(lst):
    return list(set(lst))

print("FIND UNIQUE ELEMENTS IN LIST")


numbers = [1, 2, 3, 2, 4, 5, 3, 6, 7, 2, 8]
strings = ["apple", "banana", "apple", "cherry", "banana", "date"]

print(f"\nList 1: {numbers}")
print(f"Unique Elements: {sorted(unique(numbers))}")

print(f"\nList 2: {strings}")
print(f"Unique Elements: {sorted(unique(strings))}")