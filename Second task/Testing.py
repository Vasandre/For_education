# https://www.codewars.com//kata/54bf85e3d5b56c7a05000cf9

def number(lines):

    for i in range(len(lines)):
        lines[i] = f"{i + 1}: {lines[i]}"

    return lines
