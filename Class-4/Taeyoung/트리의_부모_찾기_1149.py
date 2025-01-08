import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())

graph = [ [] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
visited = [0]*(N+1)
result = [1]*(N+1)

while q:
    node = q.popleft()
    visited[node] = 1

    for i in graph[node]:
        if visited[i] == 0:
            q.append(i)
            visited[i] = 1
            result[i] = node

for i in range(2, N+1):
    print(result[i])

'''
메모리 : 52736 KB
시간 : 348 ms
'''