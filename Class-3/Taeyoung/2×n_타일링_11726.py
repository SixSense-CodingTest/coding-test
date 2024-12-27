import sys

input = sys.stdin.readline

n = int(input().strip())

dp = [0] * 1001

dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)

'''
메모리 : 32412 KB
시간 : 36 ms
'''


input = sys.stdin.readline

n = int(input().strip())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    prev2, prev1 = 1, 2

    for i in range(3, n+1):
        curr = (prev2 + prev1) % 10007
        prev2, prev1 = prev1, curr

    print(prev1)

'''
메모리 : 32412 KB
시간 : 40 ms
'''
