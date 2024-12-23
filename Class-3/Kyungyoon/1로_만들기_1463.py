N = int(input())
dp = {1:0}

# 2부터 N까지 최소 연산 횟수 계산
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1) # i//2로 이동한 계산을 +1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])

"""
PyPy3
메모리 : 214748 KB
시간 : 280 ms
"""