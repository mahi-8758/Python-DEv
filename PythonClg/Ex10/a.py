def cumulative_product(lst):
    result = []
    product = 1
    for num in lst:
        product *= num
        result.append(product)
    return result
print("CUMULATIVE PRODUCT")

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [2, 3, 4]
numbers3 = [5, 2, 3, 1]

print(f"\nList 1: {numbers1}")
print(f"Cumulative Product: {cumulative_product(numbers1)}")

print(f"\nList 2: {numbers2}")
print(f"Cumulative Product: {cumulative_product(numbers2)}")

print(f"\nList 3: {numbers3}")
print(f"Cumulative Product: {cumulative_product(numbers3)}")