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
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /, ^, %): ")
    if operation in calculator:
        result = calculator[operation](a,b)
        print(f"{a} {operation} {b} = {result}")
    reuse = input("Wanted to reuse the answer?  Type 'yes' or 'no'").lower()
    if reuse == 'yes':
        a = result
        b = float(input("Enter next number: "))
        operation = input("Enter operation (+, -, *, /, ^, %): ")
        if operation in calculator:
            result = calculator[operation](a,b)
            print(f"{a} {operation} {b} = {result}")
    elif reuse == 'no':
        return


print("Welcome to the Calculator!")
calcontinue = 'yes'
while calcontinue.lower() == 'yes':
    calculator()
    calcontinue = input("Want to continue? (yes/no)") 
    if calcontinue is 'no':
        print("Thank you for using the calculator. Goodbye!")   
    
