N = int(input())
A = list(map(int,input().split()))

dp = [1]*N

for i in range(N):
    for k in range(i):
        if A[k] < A[i]:
            dp[i] = max(dp[k]+1,dp[i])

print(max(dp))
