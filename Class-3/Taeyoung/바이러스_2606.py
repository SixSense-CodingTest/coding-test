import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
v = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = 1
Q = deque([1])

while Q:
    c = Q.popleft()

    for i in graph[c]:
        if visited[i] == 0:
            Q.append(i)
            visited[i] = 1

print(sum(visited)-1)

"""
PyPy3
메모리 : 34900 KB
시간 : 60 ms
"""
