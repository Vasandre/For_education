
# https://www.codewars.com//kata/581b30af1ef8ee6aea0015b9

def countWins(winnerList, country):
    count = 0

    for winner in winnerList:

        if country in winner.values():
            count += 1

    return count
