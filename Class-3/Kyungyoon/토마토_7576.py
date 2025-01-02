"""
DFS(깊이 우선 탐색) : 한 방향으로 깊게 탐색하고 더 탐색할 곳이 없으면 직전에 방문했던 노드로 되돌아가는 방식 
    - LIFO 
    - 스택사용(append, pop)
BFS(너비 우선 탐색) : 현재 노드와 인접한 노드들을 모두 탐색한 후, 다음 깊이로 넘어가는 방식 
    - FIFO 
    - 큐(append, popleft) : from collections import deque
    - 최단거리 찾는데 효과적(이동시간 일정한 경우)
다익스트라 알고리즘 : 이동시간이 일정하지 않고, 각 이동 방식에 따라 시간이 다르게 주어지는 경우
    - heapq(우선순위 큐, 최소 힙 : 데이터 중 가장 작은 값, 우선순위가 높은 값 빠르게 꺼내야할 때 유용)
    - heapq.heappop(heap) : 힙에서 최소값 제거 및 반환
    - heapq.heappush() : 힙에 아이템 추가
    - heapq.heapify(list) : 리스트를 힙 구조로 변환
"""
from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# BFS를 위한 큐 초기화 : 큐에는 항상 익은 토마토의 좌표가 들어감
queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i,j))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1 # box에 날짜 입력
            queue.append((nx, ny))

ans = 0
# flag로 푼 경우-------------------------------------------
flag = False

for row in box:
    for tomato in row:
        if tomato == 0: # 토마토가 모두 익지 못 하는 경우
            flag = True
            break
    if flag: # flag가 True면 밖 for문 종료
        break

if flag: # 토마토가 모두 익지 못 하는 경우
    print(-1)
else:
    ans = max(map(max, box)) # 2차원배열
    print(ans-1)

# for else로 푼 경우----------------------------------------
for row in box:
    for tomato in row:
        if tomato == 0:
            print(-1)
            break
    else: # 안쪽 반복문이 정상종료된 경우 = 토마토 익음
        continue # 밖 반복문으로 계속
    break 
else: # 안쪽 반복문이 정상종료된 경우 = 모든 토마토 익음
    ans = max(map(max, box)) 
    print(ans-1)