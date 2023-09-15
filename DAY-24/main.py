import os

path_to_names = "Input/Names/invited_names.txt"
path_to_letter = "Input/Letters/starting_letter.txt"
path_to_output = "Output/ReadyToSend"
name_path = os.path.abspath(f"DAY-24/{path_to_names}")
letter_path = os.path.abspath(f"DAY-24/{path_to_letter}")
output = os.path.abspath(f"DAY-24/{path_to_output}")


with open(name_path) as data:
    names = data.read().split('\n')
with open(letter_path) as letter_data:
    letter = letter_data.read()

for name in names:
    new_letter = letter.replace('[name]', name)
    with open(output+f"/letter_for_{name}.txt", mode='w') as file:
        file.write(new_letter)



#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp