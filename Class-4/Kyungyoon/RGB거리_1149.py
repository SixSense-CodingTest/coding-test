N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]

# 첫번째 집 R,G,B로 칠했을 때 비용
dp[0][0] = costs[0][0]
dp[0][1] = costs[0][1]
dp[0][2] = costs[0][2]

for i in range(1, N):
    # dp 순차적 진행 -> i-1과의 관계만 고려
    dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2]) # 현재 R 색칠비용 + 이전 집 G, B 중 min값
    dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))

"""
PyPy3
메모리 : 110708 KB
시간 : 104 ms
"""