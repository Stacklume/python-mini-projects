import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password =  []
print("Welcome to the PyPassword Generator!")
let = int(input("How many letters would you like in your password?"))
sym= int(input("How many symbols would you like?"))
num= int(input("How many numbers would you like?"))
for char in range(1, let + 1):
    let_added=random.choice(letters)
    password += let_added
for char in range(1, sym + 1):
    sym_added=random.choice(symbols)
    password += sym_added
for char in range(1, num + 1):
    num_added=random.choice(numbers)
    password += num_added
random.shuffle(password)
print(f"Your password is: {password}")