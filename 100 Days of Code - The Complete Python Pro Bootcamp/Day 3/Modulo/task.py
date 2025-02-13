user_input = int(input("Please enter a number:"))
divide_by = int(input("Please enter the number by which to divide:"))

modulos= user_input % divide_by
if  modulos==0:
    print(f"{user_input} is completely divided by {divide_by}")
else:
    print(f"{user_input} when divided by {divide_by}, returns remainder: {modulos}")
