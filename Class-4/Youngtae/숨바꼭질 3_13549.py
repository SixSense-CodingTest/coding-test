# 수빈 => 현재 점 N 동생 => 점 K
# 1초 후에 X-1 X+1로 이동 가능
# 0초 후에 2X 위치로 이동가능
# 동생 찾는 가장 빠른 시간? bfs

# import sys
# from collections import deque
# input = sys.stdin.readline

# def find_min_time(N, K):
#     visited = [False] * 100001
#     queue = deque([(N,0)])

#     visited[N] = True
#     while queue:
#         pos, time = queue.popleft()

#         if pos == K:
#             return time

#         for move in [pos - 1, pos + 1, pos * 2]:
#             if 0<= move < 100001 and not visited[move]:
#                 visited[move] = True
#                 queue.append((move, time + (0 if move == pos * 2 else 1)))

# N, K = map(int, input().split())
# print(find_min_time(N, K))

import sys
from collections import deque
input = sys.stdin.readline

def find_min_time(N, K):
    MAX = 100001
    visited = [ -1 ] * MAX
    dq = deque()
    dq.append(N)
    visited[N] = 0

    while dq:
        current = dq.popleft()

        if current == K:
            return visited[current]

        next_pos = current * 2
        if 0 <= next_pos < MAX and visited[next_pos] == -1:
            visited[next_pos] = visited[current]
            dq.appendleft(next_pos)

        next_pos = current - 1
        if 0 <= next_pos < MAX and visited[next_pos] == -1:
            visited[next_pos] = visited[current] + 1
            dq.append(next_pos)

        next_pos = current + 1
        if 0 <= next_pos < MAX and visited[next_pos] == -1:
            visited[next_pos] = visited[current] + 1
            dq.append(next_pos)

N, K = map(int, input().split())
print(find_min_time(N, K))