n = int(input())
dp = [0] * (n+1)
for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    if i%3==0: dp[i] = min(dp[i],dp[i//3]+1)
    if i%2==0: dp[i] = min(dp[i],dp[i//2]+1)
print(dp[n])
# 40224kb
# 452ms

n = int(input())
dp = [0] * (n+1)
for i in range(2, n+1):
    dp[i] = min(dp[i-1], dp[i//3]+i%3, dp[i//2]+i%2)+1
print(dp[n])
# 40224kb
# 476ms

n = int(input())
dp = [0] * (n+1)
for i in range(2, n+1):
    dp[i] = min(dp[i//3]+i%3, dp[i//2]+i%2)+1
print(dp[n])
# 40224kb
# 432ms

n = int(input())
dp = [0,0]
for i in range(2, n+1): dp.append(min(dp[i//3]+i%3, dp[i//2]+i%2)+1)
print(dp[n])
# 40660kb
# 416ms

d = {1:0, 2:1, 3:1}
def dp(n):
    if n in d: return d[n]
    return min(dp(n//3)+n%3, dp(n//2)+n%2)+1
# 32412kb
# 44ms