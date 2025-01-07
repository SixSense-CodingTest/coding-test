############
# silver 2 #
############

import sys

input = sys.stdin.readline

number_of_items = int(input())
items = [0]
items.extend(map(int, input().split()))

dp = [0] * (number_of_items + 1)

for i in range(1, number_of_items + 1):
    dp[i] = 1
    for j in range(1, i):
        if items[j] < items[i]:
            dp[i] = max(dp[j] + 1, dp[i])

# print(dp)
print(max(dp))

###################
# memory: 32412KB #
# time:   128ms   #
###################

# 반례
# 6
# 10 20 30 25 26 27
# 5

