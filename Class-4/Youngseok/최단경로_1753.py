import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n, edge = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
for i in range(edge):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [float('INF')] * (n + 1)
dist[start] = 0
heap = [(0, start)]

while heap:
    current_dist, node = heappop(heap)
    if current_dist > dist[node]: continue
    for v, w in graph[node]:
        if current_dist + w < dist[v]:
            dist[v] = current_dist + w
            heappush(heap, (dist[v], v))

print(*map(lambda x: f'{x:.0F}',dist[1:]))
# 70516kb
# 688ms

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
print = sys.stdout.write
n, edge = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
for i in range(edge):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [10e9] * (n + 1)
dist[start] = 0
heap = [(0, start)]

while heap:
    current_dist, node = heappop(heap)
    if current_dist > dist[node]: continue
    for v, w in graph[node]:
        if current_dist + w < dist[v]:
            dist[v] = current_dist + w
            heappush(heap, (dist[v], v))

for i in range(1, n+1):
    if dist[i] == 10e9: print('INF\n')
    else: print(f'{dist[i]}\n')
# 69300kb
# 640ms