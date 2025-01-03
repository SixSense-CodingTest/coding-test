# 가로 m개 세로 n개
# 0은 갈수없는 땅, 1은 갈 수 있는 땅, 2는 목표지점
# 각 지점에서 목표지점까지의 거리 출력
# 0엔 0을 출력하고 갈수 있는 땅중에 못가면 -1 출력
# 각 위치에서의 최단거리를 구하기 BFS
# 특정 좌표에서 가로 세로 움직이면서 2를 찾으면 거리를 시작 위치에 기록 => distance에 기록
# 특정 좌표값이 0 이면 0 저장
# 0아닌데 못가면 -1 저장

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

distances = [[-1] * m for _ in range(n)] 
moves = [[-1,0], [1,0], [0,1], [0,-1]]

queue = deque()
for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            queue.append((i,j))
            distances[i][j] = 0
        elif maps[i][j] == 0:
            distances[i][j] = 0

while queue:
    x, y = queue.popleft()
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and distances[nx][ny] == -1 and maps[nx][ny] == 1:
            distances[nx][ny] = distances[x][y] + 1
            queue.append((nx,ny))

for row in distances:
    print(" ".join(map(str, row)))

# for i in range(n):
#     for j in range(m):
#         if j == m-1:
#             print(distances[i][j])
#         else:
#             print(distances[i][j], end = " ")
# def bfs(x,y):
#     queue = deque()
#     visited = [[False] * m for _ in range(n)]
#     queue.append([x,y])
#     start_x = x; start_y = y
#     visited[start_y][start_x] = True
#     distance = 0

#     if maps[start_y][start_x] == 0:
#         distances[start_y][start_x] = 0
    
#     while queue:
#         x,y = queue.popleft()
#         if maps[y][x] == 2:
#             distances[start_y][start_x] = distance
#             break
#         for dx, dy in moves:
#             nx = x + dx; ny = y + dy
#             if 0<= nx < m and 0<= ny < n and not visited[ny][nx] and not maps[ny][nx] != 0:
#                 queue.append([nx,ny])
#                 visited[ny][nx] = True
#                 distance += 1
#             else:
#                 continue

# for i in range(n):
#     for j in range(m):
#         bfs(i,j)

# for i in range(n):
#     for j in range(m):
#         if j == m-1:
#             print(distances[i][j])
#         else:
#             print(distances[i][j], end = " ")
        
    



