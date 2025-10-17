lettercap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
print("Welcome to Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_lettercap = int(input("How many capital letters would you like?\n"))
import random
password = []
for char in range(1, nr_letters + 1):        
    password += random.choice(letter)                
for char in range(1, nr_lettercap + 1):           
    password += random.choice(lettercap)
for num in range(1, nr_numbers + 1):
    password += str(random.choice(number))
for sym in range(1, nr_symbols + 1):
    password += random.choice(symbol)
random.shuffle(password)
final_password = ""
for char in password:
    final_password += char
print(f"Your password is: {final_password}")
