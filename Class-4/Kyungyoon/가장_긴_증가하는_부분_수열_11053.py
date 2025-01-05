N = int(input())
nums = list(map(int, input().split()))

dp = [1] * N 

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

"""
i=0
10,20,10,30,20,50
i=1
nums[0] < nums[1] : 10 < 20 이므로
dp[1] = max(dp[1], dp[0]+1) = max(1,2) = 2
i=2
10 = 10 (무시)
20 > 10 (무시)
i=3
10 < 30 : dp[3] = max(dp[3], dp[0]+1) = max(0, 2) = 2
20 < 30 : dp[3] = max(2, 2+1) = 3
10 < 30 : dp[3] = max(3, 1+1) = 3
"""

"""
PyPy3
메모리 : 109544 KB
시간 : 100 ms
"""