# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(sequence):
    
    current = 0
    previous = 0
    answer = []

    while previous < len(sequence):

        if not answer or sequence[current] != sequence[previous]:

            answer.append(sequence[previous])
            current = previous

        previous += 1

    return answer
