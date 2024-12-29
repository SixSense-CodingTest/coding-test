from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [[int(j) for j in input().strip()] for _ in range(N)]

q = deque()
q.append((0, 0))

while q:
    cy, cx = q.popleft()

    for i in range(4):
        ny, nx = cy + dy[i], cx + dx[i]

        if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 1:
            q.append((ny, nx))
            graph[ny][nx] = graph[cy][cx] + 1


print(graph[N-1][M-1])

'''
메모리 : 34944KB
시간 : 76ms
'''
