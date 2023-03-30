N = int(input())
M = int(input())

manka = set()
ovsyanka = set()

for _ in range(N):
    manka.add(input())

for _ in range(M):
    ovsyanka.add(input())

if (count := manka & ovsyanka):
    print(len(count))
else:
    print("Таких нет")