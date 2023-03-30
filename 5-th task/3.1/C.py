L = int(input())
N = int(input())

mas = []

for _ in range(N):
    mas.append(input())

for el in mas:
    if L < len(el):
        print(el[:L - 3] + "...")
    else:
        print(el)