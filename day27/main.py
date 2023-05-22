import pandas

alphabet = pandas.read_csv('./nato_phonetic_alphabet.csv')
df = alphabet
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}

isRunning = True
while isRunning:
    word = input("NATO Alphabet Converter. Enter a word: ").upper()
    word = [phonetic_dict[l] for l in word]
    print(word)







