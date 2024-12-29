import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())

hq = []

for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(-heapq.heappop(hq))
    else:
        heapq.heappush(hq, -x)

'''
메모리 : 38340 KB
시간 : 120 ms
'''
