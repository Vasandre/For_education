# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(sequence):

    current = 0
    answer = []

    while current < len(sequence):

        if not answer or sequence[current] != answer[-1]:

            answer.append(sequence[current])

        current += 1

    return answer
