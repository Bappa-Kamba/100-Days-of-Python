import pandas

data = pandas.read_csv("DAY-30\\NATO-Alphabets\\nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (_, row) in data.iterrows()}

while True:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        
    except KeyError:
        print("Sorry only letters are allowed.")

    else:
        print(output_list)
        break
