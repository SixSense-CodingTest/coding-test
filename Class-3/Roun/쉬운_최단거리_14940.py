############
# silver 1 #
############

import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, target: tuple):
    target = *target, 0
    visited = [[-1 for _ in range(len(graph[0]))] for _ in range(len(graph))]
    visited[target[0]][target[1]] = 0
    queue = deque([target])

    while queue:
        row, col, distance = queue.popleft()

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            y = row + dy
            x = col + dx

            if 0 <= y < len(graph) and 0 <= x < len(graph[0]):
                if visited[y][x] == -1:
                    if not graph[y][x] == 0:
                        queue.append((y, x, distance + 1))
                        visited[y][x] = distance + 1
                    else:
                        visited[y][x] = 0
        
    return visited

row, col = map(int, input().split())

graph = []

for i in range(row):
    line = list(map(int, input().split()))
    if 2 in line:
        start_point = (i, line.index(2))
    graph.append(line)

visited = bfs(graph, start_point)

# visitied 결과에서 원래 벽인 부분은 0으로 바꿔주는 작업 필요
# 그 쪽으로 방문 안했을 때, -1로 처리되어 있는 경우 수정
result = [[0 if graph[i][j] == 0 else visited[i][j] for j in range(col)] for i in range(row)]

for line in result:
    print(' '.join(map(str, line)))

###################
# memory: 43920KB #
# time:   412ms   #
###################

