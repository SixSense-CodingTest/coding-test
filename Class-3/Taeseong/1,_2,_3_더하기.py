T = int(input())


dp = [0]*12

dp[1] = 1
dp[2] = 2 
dp[3] = 4 



def solv(n):

    if n <= 0:
        return 0

    if dp[n]!=0:
        return dp[n]
    
    res = solv(n-1) + solv(n-2) + solv(n-3)

    dp[n] = res

    return res 



for _ in range(T):
    n = int(input())
    print(solv(n))

