
# https://www.codewars.com//kata/5963c18ecb97be020b0000a2

def derive(coefficient, exponent):
    multiplication = coefficient * exponent
    if exponent >= 1:
        exponent -= 1

    decision = str(multiplication) + "x^" + str(exponent)

    return decision