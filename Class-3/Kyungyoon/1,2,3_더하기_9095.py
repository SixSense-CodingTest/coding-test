T = int(input())
dp = [0] * 11 # 최댓값 10
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] # 이전 결과에 +1, +2, +3하면 되므로 경우의 수 그대로 가져와서 합함

for _ in range(T):
    N = int(input())
    print(dp[N])

"""
PyPy3
메모리 : 108384 KB
시간 : 88 ms
"""