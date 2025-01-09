T = int(input())
for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    
    # 점화식에서 이전 열 적용 불가능한 부분 따로 처리
    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue
    
    """
    아무 스티커도 선택하지 않은 경우의 점수 최댓값 : dp[0][i]
    위쪽 스티커를 선택한 경우의 점수 최댓값 : dp[1][i]
    아래쪽 스티커를 선택한 경우의 점수 최댓값 : dp[2][i]
    """
    dp = [[0] * n for _ in range(3)]
    dp[0][0] = 0
    dp[1][0] = sticker[0][0]
    dp[2][0] = sticker[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])
        dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + sticker[0][i] # 위쪽 스티커를 선택하려면 이전 열에서 아무것도 선택하지 않았거나 아래쪽 스티커를 선택한 상태
        dp[2][i] = max(dp[0][i-1], dp[1][i-1]) + sticker[1][i] # 아래쪽 스티커를 선택하려면 이전 열에서 아무것도 선택하지 않았거나 위쪽 스티커를 선택한 상태

    print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))

"""
dp[0][1] = max(0,50,30) = 50
dp[1][1] = max(0,30) + 10 = 40
dp[2][1] = max(0,50) + 50 = 100

dp[0][2] = max(50,40,100) = 100
dp[1][2] = max(50,100) + 100 = 200
dp[2][2] = max(50,40) + 70 = 120
"""
"""
PyPy3
메모리 : 180744 KB
시간 : 280 ms
"""