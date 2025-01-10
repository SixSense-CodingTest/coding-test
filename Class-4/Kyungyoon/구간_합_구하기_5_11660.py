N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        # dp[i][j] : (1,1)에서 (i,j)까지 누적합
        # dp[i-1][j] : 위쪽까지 누적합
        # dp[i][j-1] : 왼쪽까지 누적합
        # dp[i-1][j-1] : 겹치는 영역
        dp[i][j] = matrix[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1] # dp[i][j]가 (1,1)부터니까 맞게 구간합 계산
    print(result)

"""
PyPy3
메모리 : 129572 KB
시간 : 3124 ms
"""