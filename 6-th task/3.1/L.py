# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/8Ymb2732go

N = int(input())

porridge = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
length = len(porridge)
el = 0
for _ in range(N):
    if el == length:
        el = 0
    print(porridge[el])
    el += 1