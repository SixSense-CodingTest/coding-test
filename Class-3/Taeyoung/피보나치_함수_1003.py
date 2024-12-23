import sys

input = sys.stdin.readline
T = int(input().strip())
cases = [int(input().strip()) for _ in range(T)]
max_cases = max(cases)

dp = [[0, 0] for _ in range(max(2, max_cases + 1))]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, max_cases+1):
    dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]

print(dp)
for i in cases:
    print(dp[i][0], dp[i][1])

'''
메모리 : 32412 KB
시간 : 32 ms
'''