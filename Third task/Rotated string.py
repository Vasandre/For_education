def is_rotation(s1, s2):
    first = 0
    second = 0

    if s1 == '' and s2 == '':
        return True

    if len(s1) != len(s2):
        return False

    while second < len(s2):

        if first == len(s1):
            first = 0

        if s1[first] != s2[second]:
            return False

        first += 1
        second += 1

        if second == len(s2) and first != len(s1):
            return False

    return True


print(is_rotation('hello', 'ohell'))