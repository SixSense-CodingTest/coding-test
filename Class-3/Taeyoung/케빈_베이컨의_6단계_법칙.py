import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())

    graph[A].append(B)
    graph[B].append(A)


def bfs(start):
    q = deque()
    q.append(start)
    relation = [0] * (N+1)

    while q:
        h = q.popleft()

        for i in graph[h]:
            if relation[i] == 0:
                relation[i] = relation[h] + 1
                q.append(i)

    return sum(relation)


result = dict()
for i in range(1, N+1):
    result[i] = bfs(i)

print(sorted(result.items(), key=lambda x: (x[1], x[0]))[0][0])

'''
메모리 : 34952KB
시간 : 56ms
'''
