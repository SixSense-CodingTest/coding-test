############
# silver 1 #
############

import sys
from collections import deque

input = sys.stdin.readline

curr, target = map(int, (input().split()))

MAX = 10**5
visited = [False] * (MAX + 1)

queue = deque([(curr, 0)])

while queue:
    pos, time = queue.popleft()

    if pos == target:
        print(time)
        break 

    if 0 <= pos - 1 <= MAX and not visited[pos - 1]:
        visited[pos - 1] = True
        queue.append((pos - 1, time + 1))
    
    if 0 <= pos + 1 <= MAX and not visited[pos + 1]:
        visited[pos + 1] = True
        queue.append((pos + 1, time + 1))
    
    if 0 <= pos * 2 <= MAX and not visited[pos * 2]:
        visited[pos * 2] = True
        queue.append((pos * 2, time + 1))


###################
# memory: 36700KB #
# time:   128ms   #
###################
