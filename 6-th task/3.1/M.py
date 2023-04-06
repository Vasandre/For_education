# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/YOO7ZFJH4A

N = int(input())
numbers = []

for _ in range(N):
    numbers.append(int(input()))

P = int(input())

for num in range(len(numbers)):
    numbers[num] = numbers[num] ** P
    print(numbers[num])