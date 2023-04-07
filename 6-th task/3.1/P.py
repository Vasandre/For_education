# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/LGkorFrReo

L = int(input()) - 3
N = int(input())

line_list = []

for line in range(N):
    line_list.append(input())

for line in line_list:
    if L >= len(line):
        L -= len(line)

        if L <= 0:
            print(line + "...")
            break
        else:
            print(line)
            
    else:
        print(line[:L] + "...")
        break