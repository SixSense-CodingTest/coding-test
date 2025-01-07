n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)] # dp[i][j] : i번째 줄 j번째 위치까지의 최대합
dp[0][0] = nums[0][0]

for i in range(1, n): 
    for j in range(i + 1):
        if j == 0: # 맨 왼쪽
            dp[i][j] = dp[i-1][j] + nums[i][j] # 현재 숫자 기준 위의 숫자 2개 중 왼쪽은 열이 다르고, 오른쪽은 열이 같다
        elif j == i: # 맨 오른쪽
            dp[i][j] = dp[i-1][j-1] + nums[i][j] 
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + nums[i][j] # 현재 숫자 기준 위의 숫자 2개 비교

print(max(dp[n-1]))

"""
PyPy3
메모리 : 111672 KB
시간 : 116 ms
"""