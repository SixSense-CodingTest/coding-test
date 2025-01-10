# 맨 위부터 아래층 내려올 때 선택된 수 합 최대가 되게
# 해당 층에서 뽑힌 index를 기록 그 index와 같거나 +1인 값중에서 최대인값 선택
# 항상 큰겂만 고르는 게 정답은 아님
# 동일 index와 index + 1의 숫자들을 더해가면서 최종에서 max 구하면 될듯

import sys
input = sys.stdin.readline


n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (i + 1) for i in range(n)]
dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            # 삼각형의 왼쪽 가장자리
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i:
            # 삼각형의 오른쪽 가장자리
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            # 대각선 왼쪽 또는 대각선 오른쪽에서 오는 경우
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))

