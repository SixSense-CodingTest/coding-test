N,K = list(map(int,input().split()))

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    W,V = list(map(int,input().split()))

    for j in range(1,K+1):
        if j<W:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],V+dp[i-1][j-W])

print(dp[-1][-1])
