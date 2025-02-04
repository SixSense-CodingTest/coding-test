from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        n = q.popleft()

        for i in graph[n]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)


cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)

'''
메모리 : 66932KB
시간 : 680ms
'''


input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(start):
    q = []
    q.append(start)

    while q:
        n = q.pop()

        if not visited[n]:
            visited[n] = 1

            for neighbor in reversed(graph[n]):
                if not visited[neighbor]:
                    q.append(neighbor)


cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)
'''
메모리 : 70060KB
시간 : 792ms
'''
