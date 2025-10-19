"""Write a program that checks if a given year is a leap year or not.
Implement the logic for leap years (divisible by 4 but not by 100 unless
also divisible by 400)."""
yrs = int(input("Enter the year: "))
if yrs % 4 == 0 and yrs % 100 != 0 or yrs % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")