import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

rand_characters = ""

for i in range(nr_letters):
    rand_characters+=random.choice(letters)
for i in range(nr_numbers):
    rand_characters+=random.choice(numbers)
for i in range(nr_symbols):
    rand_characters += random.choice(symbols)

print(rand_characters)

#Simple level
simple_password = ""
for i in rand_characters:
    simple_password += i

print(f"Your simple password is: {simple_password}")

#Hard level
hard_password = ''.join(random.sample(rand_characters, len(rand_characters)))

print(f"Your hard password is {hard_password}")

