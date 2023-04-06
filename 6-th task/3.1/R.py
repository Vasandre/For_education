# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/R3wYYWsSR8

string = input()
count = 1
stack = []

for ch in string:

    if not stack:
        stack.append([ch, str(count)])
    
    elif ch == stack[0][0]:
        count += 1
        stack[0][1] = str(count)
        
    elif ch != stack[0][0]:
        print(" ".join(stack.pop()))
        count = 1
        stack.append([ch, str(count)])

print(" ".join(stack.pop()))