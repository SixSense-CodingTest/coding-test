############
# silver 1 #
############

import sys
from collections import deque


input = sys.stdin.readline

size = int(input())

graph = []

for i in range(size):
    graph.append(list(map(int, input().split())))

dp = [[0] * size for _ in range(size)]

dp[0][0] = graph[0][0]

for i in range(1, size):
    for j in range(i + 1):
        if j == 0:
            # 가장 왼쪽
            dp[i][j] = dp[i - 1][j] + graph[i][j]
        elif j == i:
            # 가장 오른쪽
            dp[i][j] = dp[i - 1][j - 1] + graph[i][j]
        else:
            # 가운데 (2개 중에 최댓값 선택)
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + graph[i][j]

print(max(dp[size - 1]))


###################
# memory: 43708KB #
# time:   144ms   #
###################