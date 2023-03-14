def to_camel_case(text):
    current = 0
    previous = 1
    answer = ""

    while current < len(text):

        if text[current] == "-" or text[current] == "_":
            answer += text[previous].upper()
            current += 1
            previous += 1

        else:
            answer += text[current]

        current += 1
        previous += 1

    return answer