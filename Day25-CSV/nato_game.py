student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
name=input("Enter your Name:")

try:
    #TODO 1. Create a dictionary in this format:
    nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
    nato_dict={ row.letter:row.code for (index,row) in nato_data.iterrows() }
    #print(nato_dict)

    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    letters= [nato_dict[key.upper()] for key in name ]
    print(letters)
except KeyError:
    print("Sorry Only Letters in the Alphabet please.")
