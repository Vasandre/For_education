line_dict = dict()

while (line := input()) != "":

    for word in line.split():
        if word in line_dict:
            line_dict[word] += 1
        else:
            line_dict[word] = 1

for watch, count in line_dict.items():
    print(watch, count)