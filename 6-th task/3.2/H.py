# https://new.contest.yandex.ru/41238/problem?id=149944/2022_10_13/HACxqMEpWL

N = int(input())
line_dict = {}

for _ in range(N):
    line = input().split()
    
    for porride in line[1:]:
        if porride in line_dict.keys():
            line_dict[porride].append(line[0])
        else:
            line_dict[porride] = [line[0]]

last_line = input()

if last_line not in line_dict.keys():
    print("Таких нет")

else:
    for word in sorted(line_dict[last_line]):
        print(word)