############
# silver 3 #
############

import sys

input = sys.stdin.readline

num = int(input())
targets = []

for _ in range(num):
    targets.append(int(input()))

dp = [0] * (max(targets) + 1)
dp[0] = 1

for i in range(1, len(dp)):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = dp[i - 1] + dp[i - 2]
    elif i >= 3:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for target in targets:
    print(dp[target])

###################
# memory: 32412KB #
# time:   32ms    #
###################