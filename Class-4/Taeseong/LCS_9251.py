A = list(input())
B = list(input())

dp = [[0]*(len(B)+1) for i in range(len(A)+1)]

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):

        if A[i-1] == B[j-1]:
            # if i>0 and j>0:
            dp[i][j] = dp[i - 1][j - 1] + 1
            
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])