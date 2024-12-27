N = int(input())

dp = [0]*1001
dp[1] = 1 
dp[2] = 2 

for i in range(3,N+1):
    dp[i] = dp[i-1] + dp[i-2] 
    
print(dp[N]%10007)