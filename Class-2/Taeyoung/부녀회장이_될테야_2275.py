import sys
input = sys.stdin.readline

T = int(input())


dp =  [[0] * (14+1) for _ in range(14+1)]

for i in range(15):
    dp[0][i] = i+1
    dp[i][0] = 1

for i in range(1, 14+1):
    for j in range(1, 14+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

for i in range(T):
    k = int(input())
    n = int(input())

    print(dp[k][n-1])

'''
메모리 : 32412KB
시간 : 36ms
'''