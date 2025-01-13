"""
DFS : 모든 경우의 수 탐색해야하는 문제, 특정 지점을 지나거나, 특정 순서대로 방문해야하는 문제 (최단거리를 보장하지 않음)
BFS : 최단거리, 최단시간 문제
"""
from collections import deque
MAX = 100000
visited = [-1] * (MAX+1) # visited[i] : i번째 위치까지 가는데 걸린 시간
N, K = map(int, input().split())
queue = deque([N])
visited[N] = 0

while queue:
    cur = queue.popleft()
    if cur == K:
        print(visited[cur])
        break
    
    # 순간이동
    if 0 <= cur * 2 <= MAX and visited[cur * 2] == -1:
        visited[cur * 2] = visited[cur] # 0초
        queue.appendleft(cur * 2) # 걷기보다 우선처리 - 0초의 효율적인 노드 먼저 그려두기
    # 걷기
    for next_p in (cur - 1, cur + 1):
        if 0 <= next_p <= MAX and visited[next_p] == -1:
            visited[next_p] = visited[cur] + 1
            queue.append(next_p)


# 시간초과
# from collections import deque
# MAX = 100000
# visited = [0] * (MAX+1) # visited[i] : i번째 위치까지 가는데 걸린 시간
# N, K = map(int, input().split())
# queue = deque([N])

# while queue:
#     cur = queue.popleft()
#     if cur == K:
#         print(visited[cur])
#         break
    
#     # 순간이동
#     if 0 <= cur * 2 <= MAX and not visited[cur * 2]:
#         visited[cur * 2] = visited[cur] # 0초
#         queue.appendleft(cur * 2) # 걷기보다 우선처리 - 0초의 효율적인 노드 먼저 그려두기
#     # 걷기
#     for next_p in (cur - 1, cur + 1):
#         if 0 <= next_p <= MAX and not visited[next_p]:
#             visited[next_p] = visited[cur] + 1
#             queue.append(next_p)

"""
PyPy3
메모리 : 112928 KB
시간 : 116 ms
"""