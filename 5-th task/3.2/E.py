N = int(input())
M = int(input())

manka = set()
ovsyanka = set()

for _ in range(N + M):
    if (word := input()) in manka:
        ovsyanka.add(word)
    else:
        manka.add(word)

if answer := manka ^ ovsyanka:
    print(len(answer))
else:
    print("Таких нет")