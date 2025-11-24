def nearly_equal(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    
    if len(a) == len(b):
        diff_count = sum(1 for i in range(len(a)) if a[i] != b[i])
        return diff_count == 1
    
    if len(a) < len(b):
        a, b = b, a
    
    for i in range(len(b)):
        if a[i] != b[i]:
            return a[i+1:] == b[i:]
    
    return True

print("NEARLY EQUAL STRINGS")
test_cases = [
    ("cat", "bat"),
    ("hello", "hallo"),
    ("abc", "ab"),
    ("python", "python"),
    ("test", "testing"),
]

for str1, str2 in test_cases:
    result = nearly_equal(str1, str2)
    print(f"'{str1}' and '{str2}': {result}")