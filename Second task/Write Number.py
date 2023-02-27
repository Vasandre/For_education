# https://www.codewars.com//kata/5842df8ccbd22792a4000245

def expanded_form(num):
    str_num = str(num)

    answer = str_num[0].zfill(len(str_num))[::-1]

    for symbol in range(1, len(str_num)):

        if int(str_num[symbol]) != 0:
            answer += " + " + str_num[symbol].zfill(len(str_num) - symbol)[::-1]

    return answer
