from collections import deque
import sys

input = sys.stdin.readline

N = int(input().strip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [[int(i) for i in input().strip()] for _ in range(N)]
visited = [[0]*N for _ in range(N)]


def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    cnt = 1

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] == 1 and visited[ny][nx] == 0:
                q.append((ny, nx))
                visited[ny][nx] = 1
                cnt += 1

    return cnt


result = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and graph[i][j] == 1:
            result.append(bfs(i, j))

print(len(result))
print("\n".join(map(str, sorted(result))))

'''
메모리 : 34944KB
시간 : 60ms
'''