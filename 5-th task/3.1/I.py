while (line := input()) != "":

    if (i := line.find("#")) != -1:
        if i != 0:
            print(line[:i])
    else:
        print(line)