n = int(input())
dp = [0]*1001
dp[1] = 1
dp[2] = 2
# dp[3] = 3
# dp[4] = 5

for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)

"""
PyPy3
메모리 : 108384 KB
시간 : 92 ms
"""