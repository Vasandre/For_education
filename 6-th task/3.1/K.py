# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/pKCFLSCyj7

N = int(input())
string_list = []

for _ in range(N):
    string_list.append(input())

request = input()

for lines in string_list:
    if request.lower() in lines.lower():
        print(lines)