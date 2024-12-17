##########
# gold 5 #
##########

import sys
from collections import deque

def bfs(graph: list):
    visited = set()
    queue = deque()

    height = len(graph)
    row = len(graph[0])
    col = len(graph[0][0])
    max_time = 0

    for h in range(height):
        for r in range(row):
            for c in range(col):
                if graph[h][r][c] == 1:
                    visited.add((h, r, c))
                    queue.append((h, r, c, 0))

    while queue:
        curr_h, curr_r, curr_c, curr_time = queue.popleft()
        max_time = max(max_time, curr_time)

        for dh, dr, dc in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            h, r, c = curr_h + dh, curr_r + dr, curr_c + dc

            if 0 <= h < height and 0 <= r < row and 0 <= c < col:
                if (h, r, c) not in visited and graph[h][r][c] == 0:
                    visited.add((h, r, c))
                    queue.append((h, r, c, curr_time + 1))

    for h in range(height):
        for r in range(row):
            for c in range(col):
                if graph[h][r][c] == 0:
                    if (h, r, c) not in visited:
                        return -1
                    
    return max_time

input = sys.stdin.readline

col, row, height = map(int, input().split())
graph = []

for i in range(height):
    temp = []
    for j in range(row):
        temp.append(list(map(int, input().split())))

    graph.append(temp)

print(bfs(graph=graph))

####################
# memory: 143640KB #
# time:   2808ms   #
####################