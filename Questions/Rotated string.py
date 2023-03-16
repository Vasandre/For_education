def is_rotation(s1, s2):

    first = 0
    second = 0

    if s1 == '' and s2 == '':
        return True

    if len(s1) != len(s2):
        return False

    for second in range(len(s2)):

        if first == len(s1):
            first = 0

        while s1[first] != s2[second]:
            first += 1

        if s1[first] == s2[second]:
            first += 1

    if first < len(s1) and s1[first] == s2[second]:
        return True

    return False


print(is_rotation('hello', 'hello'))