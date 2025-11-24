def reverse(lst):
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result
print("REVERSE A LIST")

numbers = [1, 2, 3, 4, 5]
strings = ["apple", "banana", "cherry", "date"]
mixed = [1, "hello", 3.14, True]

print(f"\nList 1: {numbers}")
print(f"Reversed: {reverse(numbers)}")

print(f"\nList 2: {strings}")
print(f"Reversed: {reverse(strings)}")

print(f"\nList 3: {mixed}")
print(f"Reversed: {reverse(mixed)}")