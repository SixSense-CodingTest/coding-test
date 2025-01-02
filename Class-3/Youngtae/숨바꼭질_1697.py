# 수빈 -> 현재 점 N, 걷거나 순간이동 가능
# 동생 -> 현재 점 K
# 걸으면 X-1 X+1 위치로 이동
# 순간이동하면 1초 후에 2*X 위치로 이동
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간 출력
# 느낌이 계속 모든 경로를 탐색하고 그중에 최단시간 출력하게 하면 될 느낌


# N, K = map(int, input().split())
# count_min = 100000

# def find_sister(x,y,count):
#     if x == y and count < count_min:
#         count_min = count
#     else:
#         find_sister(x*2, y, count + 1)
#         find_sister(x+1, y, count + 1)
#         find_sister(x-1, y, count + 1)

# find_sister(N, K, 0)

import sys
input = sys.stdin.readline
from collections import deque

def find_min_time(N, K):
    visited = [False] * 100001
    queue = deque((N,0))

    visited[N] = True
    while queue:
        pos, time = queue.popleft()

        if pos == K:
            return time

        for move in [pos + 1, pos - 1, pos * 2]:
            if 0<= move < 100001 and not visited[move]:
                visited[move] = True
                queue.append((move, time + 1))

N, K = map(int, input().split())

print(find_min_time(N, K))


    

