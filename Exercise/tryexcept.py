try :
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")