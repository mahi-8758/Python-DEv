print("\n" + "=" * 40)
print("INDENTATION ERROR EXAMPLE")
print("\n1. CODE WITH INDENTATION ERROR:")
code_with_error = """
def greet(name):
print(f"Hello, {name}!")
greet("Alice")
"""
print(code_with_error)
print("ERROR: IndentationError - expected an indented block")
print("\n2. CORRECTED CODE:")
code_corrected = """
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
"""
print(code_corrected)
print("\n3. RUNNING CORRECTED CODE:")
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
greet("Bob")
print("KEY POINT: Always indent inside functions/loops!")
print("=" * 40)