import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=""
pass_chr_list=[]
for ind in range(0,nr_letters):
    let=random.choice(letters)
    password+=let
    pass_chr_list.append(let)
for ind in range(0,nr_symbols):
    # symbols[random.randint(0,len(symbols))]
    let = random.choice(symbols)
    password += let
    pass_chr_list.append(let)
for ind in range(0,nr_numbers):
    let = random.choice(numbers)
    password += let
    pass_chr_list.append(let)

print(password)
random.shuffle(pass_chr_list)
print(''.join(pass_chr_list))

char_arr = list(range(1,len(password)))
for index in range(1,len(password)):
    print(index)