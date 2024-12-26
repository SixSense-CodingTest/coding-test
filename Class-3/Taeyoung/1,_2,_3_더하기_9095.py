import sys

input = sys.stdin.readline

T = int(input().strip())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(T):
    print(dp[int(input().strip())])

'''
메모리 : 32412 KB
시간 : 36 ms
'''
