##########
# gold 5 #
##########

import sys
from collections import deque

def bfs(cur: int, tgt: int) -> int:
    queue = deque([(cur, 0)])
    visited = set([cur])

    while queue:
        loc, time = queue.popleft()

        if loc == tgt:
            return time

        # 순간이동은 시간이 들지 않아 우선 탐색
        # 1 -> [(2, 0), (0, 1), (2, 1)]
        for i, new_loc in enumerate([loc*2, loc-1, loc+1]):
            if 0 <= new_loc <= 10**5 and new_loc not in visited:
                if i != 0:
                    queue.append((new_loc, time + 1))
                else:
                    if new_loc == tgt:
                        return time
                    queue.appendleft((new_loc, time))
                visited.add(new_loc)
        

input = sys.stdin.readline

current, target = map(int, input().split())

print(bfs(current, target))

###################
# memory: 42336KB #
# time:   128ms   #
###################