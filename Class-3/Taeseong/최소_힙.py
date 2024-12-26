import heapq
import sys

input = sys.stdin.readline

N = int(input().strip())

H = []
for _ in range(N):

    n = int(input().strip())
    if n == 0:
        if len(H)>0:
            print(heapq.heappop(H))
        else:
            print(0)

    else:
        heapq.heappush(H,n)
