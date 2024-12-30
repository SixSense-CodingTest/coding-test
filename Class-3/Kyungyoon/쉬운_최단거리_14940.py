"""
DFS(깊이 우선 탐색) : 한 방향으로 깊게 탐색하고 더 탐색할 곳이 없으면 직전에 방문했던 노드로 되돌아가는 방식 
    - LIFO 
    - 스택사용(append, pop)
BFS(너비 우선 탐색) : 현재 노드와 인접한 노드들을 모두 탐색한 후, 다음 깊이로 넘어가는 방식 
    - FIFO 
    - 큐(append, popleft)
    - 최단거리 찾는데 효과적(이동시간 일정한 경우)
다익스트라 알고리즘 : 이동시간이 일정하지 않고, 각 이동 방식에 따라 시간이 다르게 주어지는 경우
    - heapq(우선순위 큐, 최소 힙 : 데이터 중 가장 작은 값, 우선순위가 높은 값 빠르게 꺼내야할 때 유용)
    - heapq.heappop(heap) : 힙에서 최소값 제거 및 반환
    - heapq.heappush() : 힙에 아이템 추가
    - heapq.heapify(list) : 리스트를 힙 구조로 변환
"""
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(n)]

distances = [[-1]*m for _ in range(n)] # 결과저장 초기화

# 타겟 찾기
target = None
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            target = (i, j)
            distances[i][j] = 0
            break
    if target:
        break

# BFS 초기화
queue = deque([target])
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 탐색
while queue:
    x, y = queue.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        # distances[nx][ny] == -1 <- 방문 안 함
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and distances[nx][ny] == -1:
            distances[nx][ny] = distances[x][y] + 1
            queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            distances[i][j] = 0
        
for row in distances:
    print(*row)

"""
PyPy3
메모리 : 120176 KB
시간 : 212 ms
"""