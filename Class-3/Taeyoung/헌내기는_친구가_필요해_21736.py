from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [input().strip() for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            s_x, s_y = j, i
            break


visited = [[0]*M for _ in range(N)]

q = deque()
q.append((s_y, s_x))
visited[s_y][s_x] = 1

cnt = 0
while q:
    cy, cx = q.popleft()

    for i in range(4):
        ny, nx = cy + dy[i], cx + dx[i]

        if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and graph[ny][nx] != 'X':
            if graph[ny][nx] == 'P':
                cnt += 1
            visited[ny][nx] = 1
            q.append((ny, nx))

print('TT' if cnt == 0 else cnt)

'''
메모리 : 39028 KB
시간 : 756 ms
'''
