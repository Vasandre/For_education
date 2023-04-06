# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/cXCfPpVk3a

numbers = input().split()

length = len(numbers)

for el in range(length):
    numbers[el] = int(numbers[el])

num_1 = numbers[0]
num_2 = numbers[1]

count = 1

while count < length:
    
    while num_1 != 0 and num_2 != 0:
        if num_1 >= num_2:
            num_1 %= num_2
        else:
            num_2 %= num_1
    
    count += 1

    if count < length:
        if num_1 == 0:
            num_1 = numbers[count]
        else:
            num_2 = numbers[count]

print(num_1 or num_2)