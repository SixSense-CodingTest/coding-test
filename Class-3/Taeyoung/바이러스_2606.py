import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)

'''
메모리 : 38340 KB
시간 : 112 ms
'''
