############
# silver 3 #
############

import sys

input = sys.stdin.readline

dp = [0] * 1001

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = dp[1] + dp[2]

num = int(input())

for i in range(4, num+1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[num] % 10007)

###################
# memory: 32412KB #
# time:   40ms    #
###################