import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())
new_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(new_dict)
word = input("enter a word: ").upper()
out_list = [new_dict[letter] for letter in word]
print(out_list)