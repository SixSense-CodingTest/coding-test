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
N, K = map(int, input().strip().split())

max_position = 100000

visited = [False]*(max_position+1) # 방문여부체크배열
queue = deque([(N, 0)]) # (현재 위치, 현재까지의 시간) # BFS 초기화
visited[N] = True

# BFS 탐색
while queue:
    position, time = queue.popleft()
    
    # 동생 찾을 때
    if position == K:
        print(time)
        break
    
    # 현재 position에서 이동가능한 모든 위치 계산
    for next_pos in (position-1, position+1, position*2):
        if 0 <= next_pos <= max_position and not visited[next_pos]:
            visited[next_pos] = True
            queue.append((next_pos, time+1))

"""
PyPy3
메모리 : 113960 KB
시간 : 128 ms
"""

# 다익스트라 알고리즘(공부용)
import heapq
import sys
input = sys.stdin.readline
N, K = map(int, input().strip().split())

max_position = 100000

# 최단시간배열 초기화
min_time = [float('inf')] * (max_position + 1)
min_time[N] = 0

pq = [(0, N)] # 우선순위 큐 초기화 (시간, 위치)

# 다익스트라 알고리즘 수행
while pq:
    current_time, position = heapq.heappop(pq)
    
    # 이미 더 짧은 시간에 방문한 경우 스킵
    if current_time > min_time[position]:
        continue
    
    for next_pos, weight in [(position - 1, 1), (position + 1, 1), (position * 2, 1)]:
        if 0 <= next_pos <= max_position:
            new_time = current_time + weight
            if new_time < min_time[next_pos]:
                min_time[next_pos] = new_time
                heapq.heappush(pq, (new_time, next_pos))

print(min_time[K])

"""
PyPy3
메모리 : 115636 KB
시간 : 192 ms
"""