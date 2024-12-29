import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            sy, sx = i, j
            graph[i][j] = 0
            break

q = deque()
q.append((sy, sx))
visited[sy][sx] = 0

while q:
    cy, cx = q.popleft()

    for i in range(4):
        ny, nx = cy + dy[i], cx + dx[i]
        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] != 0 and visited[ny][nx] == 0:
            graph[ny][nx] = graph[cy][cx] + 1
            visited[ny][nx] = 1
            q.append((ny, nx))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            graph[i][j] = -1

for i in graph:
    print(" ".join(map(str, i)))

'''
메모리 : 41536KB
시간 : 696ms
'''
