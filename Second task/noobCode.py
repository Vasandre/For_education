# https://www.codewars.com//kata/57470efebf81fea166001627

def letter_check(arr):

    for symbol in arr[1]:

        if arr[0].lower().find(symbol.lower()) == -1:

            return False

    return True
