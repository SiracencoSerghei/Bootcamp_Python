"""https://www.nato.int/cps/en/natohq/news_150391.htm
    https://www.nato.int/nato_static_fl2014/assets/pdf/pdf_2018_01/20180111_nato-alphabet-sign-signal.pdf
    """

import pandas

# with open("nato_phonetic_alphabet.csv") as file:
    # alphabet = file.readlines()
    
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
print(alphabet)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
alphabet_dict = {row.letter: row.code for index, row in alphabet.iterrows()}
print(alphabet_dict)
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [alphabet_dict[letter] for letter in word]
print(output_list)

