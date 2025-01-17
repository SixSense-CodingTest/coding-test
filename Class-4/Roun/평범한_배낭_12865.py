##########
# gold 5 #
##########

import sys

input = sys.stdin.readline

number_of_items, max_weight = map(int, input().split())

items = []
dp = [0] * (max_weight + 1)

for _ in range(number_of_items):
    weight, value = tuple(map(int, input().split()))

    # 앞에서 부터하면 (8, 4) (16, 8) 이렇게 중복으로 들어감
    for i in range(max_weight, weight - 1, -1):
        dp[i] = max(dp[i], dp[i - weight] + value)

    # print(dp)

print(max(dp))

    
###################
# memory: 36264KB #
# time:   2640ms  #
###################