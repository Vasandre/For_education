
# https://www.codewars.com//kata/56f699cd9400f5b7d8000b55

def fix_the_meerkat(arr):

    intermediative = arr[0]
    arr[0] = arr[-1]
    arr[-1] = intermediative

    return arr

list = ["tail", "body", "head"]
