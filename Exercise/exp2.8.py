"""Develop a program that prints the Fibonacci sequence up to a certain
number of terms. Allow the user to input the number of terms"""
num = int(input("Enter a number: "))
if num <= 0:
    print(num)
elif num == 1:
    print(num)
else:
    a, b = 0, 1
    for num in range(2, num + 1):
        print(a)
        a, b = b, a + b

