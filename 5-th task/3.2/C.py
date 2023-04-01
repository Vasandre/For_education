answer = set()
N = int(input())

for _ in range(N):
    answer = answer | set(input().split())

for word in answer:
    print(word)