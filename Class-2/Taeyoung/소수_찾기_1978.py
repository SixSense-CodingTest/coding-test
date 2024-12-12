N = int(input())

prime_numbers = list(map(int, input().split()))

result = 0

for i in prime_numbers:
    if i == 1:
        continue

    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
            break

    if cnt == 0:
        result += 1

print(result)