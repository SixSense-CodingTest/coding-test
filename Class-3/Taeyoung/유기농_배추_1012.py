from collections import deque
import sys

input = sys.stdin.readline

T = int(input().strip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, graph, visited, M, N):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]

            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx, ny))


for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0]*N for _ in range(M)]
    visited = [[0]*N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    cnt = 0

    for i in range(M):
        for j in range(N):
            if visited[i][j] == 0 and graph[i][j] == 1:
                bfs(i, j, graph, visited, M, N)
                cnt += 1

    print(cnt)

'''
메모리 : 35000KB
시간 : 64ms
'''
