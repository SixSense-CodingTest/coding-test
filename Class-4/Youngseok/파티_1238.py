import sys
from heapq import heappop, heappush
input = sys.stdin.readline
def search(n, graph, start):
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
    return dist

def solve():
    n, edge, end = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(edge):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    to_end = [0] * (n + 1)

    for start in range(1, n+1):
        dist = search(n, graph, start)

        if start == end: end_to = dist
        else: to_end[start] = dist[end]    
    print(max(end_to[x]+to_end[x] for x in range(1, n+1)))
solve()
# 35508kb
# 864ms

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
def search(n, graph, start):
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
    return dist

def solve():
    n, edge, end = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    reverse_graph = [[] for _ in range(n+1)]
    for i in range(edge):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        reverse_graph[v].append((u, w))

    end_to = search(n, graph, end)
    to_end = search(n, reverse_graph, end)

    print(max(map(lambda x: end_to[x]+to_end[x], range(1, n+1))))
solve()
# 36532kb
# 44ms
def solve():
    n, edge, end = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    reverse_graph = [[] for _ in range(n+1)]
    for i in range(edge):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        reverse_graph[v].append((u, w))

    print(max(map(sum, zip(search(n, graph, end), search(n, reverse_graph, end)))))
solve()