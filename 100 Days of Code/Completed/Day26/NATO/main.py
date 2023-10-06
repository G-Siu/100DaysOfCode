import pandas

with open("nato_phonetic_alphabet.csv") as file:
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
codeword = {row.letter: row.code for (index, row) in data.iterrows()}

word = list(input("Enter a word: ").upper())
phonetic = [codeword[letter] for letter in word]
print(phonetic)