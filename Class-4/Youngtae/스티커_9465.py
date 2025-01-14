# 스티커 떼면 왼오위아래 다 떼짐
# 점수 합 최대가 되게 스티커 떼기

import sys
input = sys.stdin.readline

T = int(input()) 

for _ in range(T):
    n = int(input()) 
    stickers = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:  # 스티커가 하나만 있을 경우
        print(max(stickers[0][0], stickers[1][0]))
        continue
    
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    dp[0][1] = dp[1][0] + stickers[0][1]
    dp[1][1] = dp[0][0] + stickers[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i]

    print(max(dp[0][n-1], dp[1][n-1]))