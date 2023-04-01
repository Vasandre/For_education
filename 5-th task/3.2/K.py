N = int(input())
surname_dict = {}
count = 0

for _ in range(N):
    surname = input()

    if surname in surname_dict:
        surname_dict[surname] += 1

    else:
        surname_dict[surname] = 1

for i in surname_dict.values():
    if i > 1:
        count += i

print(count)