def sum(a,b):
    return a + b
def subtract(a,b):  
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error! Division by zero."
    return a / b 
def power(a,b):
    return a ** b
def modulus(a,b):
    return a % b
def calculator():
    calculator = {
        '+': sum,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '^': power,
        '%': modulus
    }
    a_val = input("Enter first number: ")
    b_val = input("Enter second number: ")
    a = float(a_val)
    b = float(b_val)
    operation = input("Enter operation (+, -, *, /, ^, %): ")
    statement = True
    
    while statement:
        if operation in calculator:
            result = calculator[operation](a,b)
            print(f"{a} {operation} {b} = {result}")
            reuse = input("Wanted to reuse the answer? Type 'yes' or 'no': ").lower()

            if reuse == 'yes':
                a = result
                b_val = input("Enter next number: ")
                b = float(b_val)
                operation = input("Enter operation (+, -, *, /, ^, %): ")
                continue
            elif reuse == 'no':
                statement = False

print("Welcome to the Calculator!")
calcontinue = 'yes'
while calcontinue == 'yes':
    calculator()
    calcontinue = input("Want to continue? (yes/no)") 
    if calcontinue == 'no':
        print("Thank you for using the calculator. Goodbye!")

