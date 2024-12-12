import math
N = int(input())
num_list = list(map(int, input().split()))

ans = 0
for num in num_list:
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            break
    else:
        if num!=1:
            ans += 1
print(ans)