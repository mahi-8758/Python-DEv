print("PYTHON BASICS - INTERACTIVE vs SCRIPT")
print("=" * 50)

a, b = 10, 20
print(f"\nArithmetic: {a} + {b} = {a + b}, {a} * {b} = {a * b}")
name = "Python"
print(f"String: {name.upper()} - Length: {len(name)}")
numbers = [1, 2, 3, 4, 5]
print(f"List: {numbers} - Sum: {sum(numbers)}, Max: {max(numbers)}")
age = 25
print(f"Age {age}: {'Adult' if age >= 18 else 'Minor'}")
score = 85
grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F'
print(f"Score: {score} - Grade: {grade}")
print(f"For Loop: ", end="")
for i in range(1, 6):
    print(i, end=" ")
print(f"\n\nFunctions:")
print(f"Greet: {(lambda n: f'Hello, {n}!')('Alice')}")
print(f"Add: 5 + 3 = {(lambda x, y: x + y)(5, 3)}")
student = {"name": "John", "age": 20, "grade": "A"}
print(f"Dict: {student}")
coords = (10, 20, 30)
print(f"Tuple: {coords}")
colors = {"red", "green", "blue", "yellow"}
print(f"Set: {colors}")
print(f"\nTypes: 42={type(42).__name__}, 3.14={type(3.14).__name__}, hi={type('hi').__name__}, [1,2]={type([1,2]).__name__}")
print("INTERACTIVE INTERPRETER: python3.14.0")
print("PYTHON SCRIPT: python3 a.py")
print("=" * 50)