import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(graph, start):
    q = []
    heapq.heappush(q, (0, start))
    result = [float('inf')] * (n+1)
    result[start] = 0

    while q:
        w, v = heapq.heappop(q)

        if result[v] < w:
            continue

        for next_node, w in graph[v]:
            next_w = w + result[v]
            if next_w < result[next_node]:
                result[next_node] = next_w
                heapq.heappush(q, (next_w, next_node))

    return result


for i in range(1, n+1):
    result = dijkstra(graph, i)
    for j in range(1, n+1):
        print(result[j] if result[j] != float('inf') else 0, end=' ')
    print()

'''
메모리 : 45480 KB
시간 : 1160 ms
'''
