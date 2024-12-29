from collections import deque
import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()


def bfs():
    q = deque()
    visited = []
    q.append(V)
    visited.append(V)

    while q:
        n = q.popleft()

        for i in graph[n]:
            if i not in visited:
                visited.append(i)
                q.append(i)

    return " ".join(map(str, visited))


def dfs():
    q = []
    result = []
    q.append(V)
    visited = [0] * (N + 1)

    while q:
        n = q.pop()

        if not visited[n]:
            visited[n] = 1
            result.append(n)

            for neighbor in reversed(graph[n]):
                if not visited[neighbor]:
                    q.append(neighbor)

    return " ".join(map(str, result))


print(dfs())
print(bfs())

'''
메모리 : 35576KB
시간 : 184ms
'''
