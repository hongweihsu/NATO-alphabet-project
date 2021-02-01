import pandas

# TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(data)

data_dict = {v.letter: v.code for (k, v) in df.iterrows()}
print(data_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [data_dict[letter] for letter in word]
print(output_list)
