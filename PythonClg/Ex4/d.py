def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


print("SELECTION SORT vs INSERTION SORT")

numbers1 = [64, 34, 25, 12, 22, 11, 90]
numbers2 = [64, 34, 25, 12, 22, 11, 90]

print(f"\nOriginal Array: {numbers1}")

sorted1 = selection_sort(numbers1.copy())
print(f"Selection Sort: {sorted1}")

sorted2 = insertion_sort(numbers2.copy())
print(f"Insertion Sort: {sorted2}")



