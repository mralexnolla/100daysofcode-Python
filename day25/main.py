with open("./input/names/invited_names.txt") as names:
    names = names.readlines()

with open("./input/letters/starting_letter.txt") as letters:
    letters = letters.read()
    for name in names:
        newLetter = letters.replace("[name]", name.strip())
        with open(f"./output/readyToSend/letter_for_{name}.txt", "w") as completed_letter:
            completed_letter.write(newLetter)
