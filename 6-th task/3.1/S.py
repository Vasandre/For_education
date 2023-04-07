# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/DnuaPWomud

string = input().split()
stack = []

for ch in string:
    if ch in "*+-":
        b = int(stack.pop())
        a = int(stack.pop())
        
        if ch == "*":
            a = a * b
        elif ch == "-":
            a = a - b
        elif ch == "+":
            a = a + b
        stack.append(a)
    else:
        stack.append(ch)

print(stack[0])