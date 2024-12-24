import sys

N = int(sys.stdin.readline().strip())

dp = [0]*(N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])

print(dp[N])

'''
메모리 : 40244 KB
시간 : 484 ms
'''
