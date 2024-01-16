import pandas

data = pandas.read_csv("Day 26\\nato_phonetic_alphabet.csv")
# 1. Create a dictionary in this format:
phonetic_dict = {row.letter : row.code for (index, row) in data.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)