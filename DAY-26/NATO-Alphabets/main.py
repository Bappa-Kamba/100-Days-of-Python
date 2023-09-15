import pandas
import os

filename = os.path.abspath('DAY-26/NATO-Alphabets/nato_phonetic_alphabet.csv')

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_alphabets = pandas.read_csv(filename)

nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabets.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()
nato_letters = [nato_alphabet_dict[letter] for letter in user_input]
print(nato_letters)

