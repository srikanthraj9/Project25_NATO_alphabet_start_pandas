import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(new_dict)

def generate_phonetic():
    word = input("enter a word: ").upper()
    try:
        out_list = [new_dict[letter] for letter in word]
    except KeyError:
        print("sorry only letters")
        generate_phonetic()
    else:
        print(out_list)

generate_phonetic()