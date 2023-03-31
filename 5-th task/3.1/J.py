word_str = ""
letters = dict()
while (line := input()) != "ФИНИШ":
    word_str += line.lower().replace(' ', '')

for abc in word_str:
    if abc not in letters:
        letters[abc] = word_str.count(abc)

print(max(letters, key=letters.get))