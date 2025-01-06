import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, graph, visited):
    q = deque()
    for y, x in start:
        q.append((y, x))
        visited[y][x] = 1

    cnt = 0
    while q:
        for _ in range(len(q)):
            cy, cx = q.popleft()

            for i in range(4):
                ny, nx = cy + dy[i], cx + dx[i]

                if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and graph[ny][nx] != -1:
                    q.append((ny, nx))
                    visited[ny][nx] = 1

        cnt += 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and graph[i][j] == 0:
                return -1
               
    return cnt-1

M, N = map(int, input().split())

start = []
graph = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j] == 1:
            start.append((i, j))

    graph.append(temp)

visited = [[0]*M for _ in range(N)]
graph_flatten = [j for i in graph for j in i ]
# if 0 not in graph_flatten and graph_flatten.count(-1) == graph_flatten.count(1):
# count가 필요없었음
# 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력하는 부분에서 헷갈려서 count를 쓴 것 같음
# if graph_flatten.count(-1) + graph_flatten.count(1) == M*N: 이걸 유도한듯
if 0 not in graph_flatten:
    print(0)
else:
    print(bfs(start, graph, visited))

'''
메모리 : 164764 KB
시간 : 1244 ms
'''