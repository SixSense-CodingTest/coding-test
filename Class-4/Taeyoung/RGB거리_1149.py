import sys
input = sys.stdin.readline

N = int(input())

RGB = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]

dp[0] = RGB[0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + RGB[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + RGB[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + RGB[i][2]

print(min(dp[N-1]))

'''
메모리 : 33432 KB
시간 : 40 ms
'''