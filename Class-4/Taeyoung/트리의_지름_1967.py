import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input().strip())

graph = defaultdict(list)

for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def bfs(graph, start):
    q = deque([(0, start)])
    visited = [-1] * (n+1)
    visited[start] = 0

    while q:
        w, v = q.popleft()

        for next_node, next_w in graph[v]:
            if visited[next_node] == -1:
                visited[next_node] = w + next_w
                q.append((visited[next_node], next_node))

    return visited

first_result = bfs(graph, 1)
final_result = bfs(graph, first_result.index(max(first_result)))

print(max(final_result))

'''
메모리 : 36508 KB
시간 : 76 ms
'''