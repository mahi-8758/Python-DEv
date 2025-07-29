"""Write a Python program that takes a user's age as input and prints whether
they are eligible to vote or not (considering the legal voting age is 18)."""
age = int(input("Enter your age: "))
print("The legal age for voting is 18")
if age < 18:
    print('Sorry to say that')
    print('You are Not Eligible for voting')
else:
    print('You are Eligible for voting')
