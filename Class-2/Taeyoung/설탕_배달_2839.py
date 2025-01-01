import sys

input = sys.stdin.readline

N = int(input().strip())

dp = [-1] * 5001
dp[3] = 1
dp[5] = 1

for i in range(6, 5001):
    if dp[i-3] != -1 and dp[i-5] != -1:
        dp[i] = min(dp[i-5], dp[i-3]) + 1
    elif dp[i-3] != -1:
         dp[i] = dp[i-3]+1
    elif dp[i-5] != -1:
        dp[i] = dp[i-5]+1

print(dp[N])

'''
메모리 : 32412KB
시간 : 40ms
'''