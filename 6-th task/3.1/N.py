# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/5vjFLZ1M9w

numbers = input().split()
P = int(input())

for num in range(len(numbers)):
    numbers[num] = str(int(numbers[num]) ** P)

print(" ".join(numbers))