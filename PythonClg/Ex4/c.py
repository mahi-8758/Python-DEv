def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = int(input("Enter a number to search: "))

print("LINEAR SEARCH vs BINARY SEARCH")
print(f"\nArray: {numbers}")
print(f"Target: {target}")

linear_result = linear_search(numbers, target)
if linear_result == -1:
    print(f"\nLinear Search: Not Found!")
else:
    print(f"\nLinear Search: Found at index {linear_result}")

binary_result = binary_search(numbers, target)
if binary_result == -1:
    print(f"Binary Search: Not Found!")
else:
    print(f"Binary Search: Found at index {binary_result}")



