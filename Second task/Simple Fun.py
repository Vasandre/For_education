# https://www.codewars.com//kata/58845748bd5733f1b300001f

def range_bit_count(a, b):
    mass = []
    count_one = 0

    for elem in range(a, b + 1):
        mass.append(elem)

        count_one += bin(elem)[2:].count('1')

    return count_one
