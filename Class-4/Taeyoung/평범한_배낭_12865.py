import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0] * (K + 1)

for _ in range(N):
    W, V = map(int, input().split())
    for i in range(K, W - 1, -1):
        dp[i] = max(dp[i], dp[i - W] + V)

print(dp[-1])

'''
메모리 : 36264 KB
시간 : 2520 ms
'''
