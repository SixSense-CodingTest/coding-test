############
# silver 1 #
############

# 1, 2번은 다른 색
# N, N-1번은 다른 색
# i번은 i-1, i+1과 다른 색

import sys

input = sys.stdin.readline

number_of_items = int(input())
costs = []

for _ in range(number_of_items):
    costs.append(list(map(int, input().split())))

dp = [[0] * 3 for i in range(number_of_items + 1)]

for i in range(3):
    dp[1][i] = costs[0][i]

for i in range(2, number_of_items + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i - 1][0] # 마지막이 R (앞이 G 또는 B 중에 최소 선택)
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i - 1][1] # 마지막이 G
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i - 1][2] # 마지막이 B

print(min(dp[number_of_items]))

###################
# memory: 44342KB #
# time:   44ms    #
###################
