import random, string

letters = string.ascii_lowercase
caps = string.ascii_uppercase
numbers = [str(i) for i in range(1, 11)]
symbols = "!@#$%^&*()"

print("Welcome to Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_lettercap = int(input("How many capital letters would you like?\n"))

password = (
    "".join(random.choice(letters) for _ in range(nr_letters)) +
    "".join(random.choice(caps) for _ in range(nr_lettercap)) +
    "".join(random.choice(numbers) for _ in range(nr_numbers)) +
    "".join(random.choice(symbols) for _ in range(nr_symbols))
)

print("Your generated password is:", password)