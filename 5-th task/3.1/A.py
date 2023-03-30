N = int(input())
list = []
count = 0
for i in range(N):
    list.append(input())
    if list[i][0] == 'а' or list[i][0] == 'б' or list[i][0] == 'в':
        count += 1
if count == N:
    print("YES")
else:
    print("NO")