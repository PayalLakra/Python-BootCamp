# NATO PROJECT

import pandas
data = pandas.read_csv("C:\\Users\\PAYAL\\Desktop\\Payal STUDY\\Python-BootCamp\\Day30\\nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for(index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word:").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letters allowed")
        generate_phonetic()
    else:
        print(output_list)