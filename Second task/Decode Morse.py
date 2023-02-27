# https://www.codewars.com//kata/54b0306c56f22d0bf9000ffb

TOME = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
        '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
        '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z', '.----': 1, '..---': 2, '...--': 3, '....-': 4,
        '.....': 5, '-....': 6, '--...': 7, '---..': 8, '----.': 9, '-----': 0}


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

print(decode(""))
