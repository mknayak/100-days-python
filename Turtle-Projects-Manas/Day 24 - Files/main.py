#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter_template=""
with open("Input/Letters/starting_letter.txt",mode="r") as letter_template_file:
    letter_template= letter_template_file.read()

names=[]

with open("Input/Names/invited_names.txt",mode="r") as names_file:
    names= names_file.readlines()

for name in names:
    name=name.strip()
    with open(f"Output/ReadyToSend/letter_for_{name}.txt",mode="w") as outfile:
        outfile.write(letter_template.replace("[name]",name))
