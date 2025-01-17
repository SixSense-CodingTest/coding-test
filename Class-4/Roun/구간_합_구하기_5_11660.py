############
# silver 1 #
############

import sys

input = sys.stdin.readline

size, number_of_cases = map(int, input().split())

graph = []

for _ in range(size):
    graph.append(list(map(int, input().split())))

for i in range(size):
    for j in range(size):
        if j != 0: graph[i][j] = graph[i][j - 1] + graph[i][j]
        if i != 0: graph[i][j] = graph[i - 1][j] + graph[i][j]
        if i != 0 and j != 0: graph[i][j] = graph[i][j] - graph[i - 1][j - 1]

for _ in range(number_of_cases):
    y1, x1, y2, x2 = map(lambda x: x-1, map(int, input().split()))
    # 2 2 3 4
    # graph[3][4] - graph[1][4] - graph[3][1] + graph[1][1]
    
    result = graph[y2][x2]

    if y1 != 0:
        result -= graph[y1 - 1][x2]
    if x1 != 0:
        result -= graph[y2][x1 - 1]
    if x1 != 0 and y1 != 0:
        result += graph[y1 - 1][x1 - 1]

    print(result)


###################
# memory: 73968KB #
# time:   1532ms  #
###################