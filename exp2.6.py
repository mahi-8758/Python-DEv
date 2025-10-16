"""Implement a program that prints the multiplication table for a given
number. Allow the user to input the number."""
num = int(input("Enter a number: "))
mul = 1
while mul <= 10:
    print(num*mul)
    mul += 1