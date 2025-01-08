import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
P = [-1]*(N+1)

for i in range(N-1):
    x,y = list(map(int,input().strip().split()))
    graph[x].append(y)
    graph[y].append(x)


Q = deque([1])


while Q:
    
    node = Q.popleft()

    for i in graph[node]:
        if P[i]!=-1:
            continue
        P[i] = node
        Q.append(i)

print(*P[2:],sep='\n')