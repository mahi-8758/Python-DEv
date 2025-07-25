"""Develop a Python script that calculates and prints the result of raising a
user-input base to a user-input exponent without using the ** operator."""
base = int(input("The given base is : "))
exponent = int(input("The given exponent is : "))
base **= exponent
print(f"The value of the given problem is {base} " )