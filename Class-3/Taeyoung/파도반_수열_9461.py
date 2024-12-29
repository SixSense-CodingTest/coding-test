import sys

input = sys.stdin.readline

T = int(input().strip())

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i-3] + dp[i-2]

for i in range(T):
    N = int(input().strip())
    print(dp[N])

'''
메모리 : 32412 KB
시간 : 32 ms
'''
