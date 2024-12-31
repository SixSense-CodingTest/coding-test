import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())

q = []

for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if len(q) == 0: print(0)
        else: print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(x), x))

'''
메모리 : 42144KB
시간 : 136ms
'''