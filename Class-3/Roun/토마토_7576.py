##########
# gold 5 #
##########

import sys
from collections import deque

def bfs(graph: list):
    visited = [[0 for i in range(len(graph[0]))] for j in range(len(graph))]
    queue = deque()
    max_time = 0

    for y in range(len(graph)):
        for x in range(len(graph[0])):
            if graph[y][x] == 1:
                # point 좌표 (y, x), time
                queue.append((y, x, 0))
                visited[y][x] = 1
            if graph[y][x] == -1:
                visited[y][x] = -1

    while queue:
        row, col, time = queue.popleft()
        max_time = max(time, max_time)

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            y, x = row + dy, col + dx

            if 0 <= x < len(graph[0]) and 0 <= y < len(graph):
                if visited[y][x] == 0 and graph[y][x] == 0:
                    queue.append((y, x, time + 1))
                    visited[y][x] = 1

    # 익지 않은 토마토가 있다면 -1 반환
    for line in visited:
        if 0 in line:
            return -1
    
    return max_time
    

input = sys.stdin.readline

col, row = map(int, input().rstrip().split())

graph = []

for i in range(row):
    graph.append(list(map(int, input().split())))

print(bfs(graph=graph))

####################
# memory: 109168KB #
# time:   1388ms   #
####################