############
# silver 3 #
############

import sys

input = sys.stdin.readline

num = int(input())
dp = [[0, 0]] * 41
dp[0] = [1, 0]
dp[1] = [0, 1]
dp[2] = [1, 1]

for i in range(3, 41):
    dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]

for i in range(num):
    target = int(input())

    print(' '.join(map(str, dp[target])))

###################
# memory: 32412KB #
# time:   32ms    #
###################