# https://www.codewars.com//kata/54b0306c56f22d0bf9000ffb


def decode(s):
    decoding = ""
    str = ""

    for elem in range(len(s)):

        str += s[elem]

        if s[elem] == " " or elem == len(s) - 1:

            word = TOME.get(str.replace(" ", ''))
            if not word:
                decoding += " "
            else:
                decoding += f'{word}'

            str = ""

    return decoding


