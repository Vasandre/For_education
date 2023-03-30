N = int(input())

for _ in range(N):
    if (pos := input().find("зайка")) != -1:
        print(pos + 1)
    else:
        print("Заек нет =(")