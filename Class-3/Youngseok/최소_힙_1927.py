import heapq
h = []
for _ in range(int(input())):
    i = int(input())
    if i: heapq.heappush(h, i)
    elif h: print(heapq.heappop(h))
    else: print(0)
# 38340kb
# 108ms

import heapq, sys
input = sys.stdin.readline
h = []
for _ in range(int(input())):
    if (i:=int(input())): heapq.heappush(h, i)
    else: print(heapq.heappop(h) if h else 0)
# 38340kb
# 104ms

import heapq, sys
input = sys.stdin.readline
print = sys.stdout.write
h = []
for _ in range(int(input())):
    if (i:=int(input())): heapq.heappush(h, i)
    else: print(f'{heapq.heappop(h)}\n' if h else '0\n')
# 38340kb
# 92ms