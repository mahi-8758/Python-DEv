"""Write a Python program that calculates the factorial of a given number
using a loop. Take the number as input"""
num = int(input("Enter a number: "))
count = 1
for num in range(1, num+1):
    count= count * num
print(count)

