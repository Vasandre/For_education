# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/zto47acz4L

line = input()

right = 0
left = len(line) - 1

while right < left:

    while line[right] == " " and right < left:
        right += 1

    while line[left] == " " and right < left:
        left -= 1

    if line[right].lower() != line[left].lower():
        print("NO")
        break

    right += 1
    left -= 1

else:
    print("YES")