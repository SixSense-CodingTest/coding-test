from collections import deque

N = int(input())
C = int(input())

graph = [[] for _ in range(N+1)]

for i in range(C):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a) 

save = set()

Q = deque([1])

while Q:

    n = Q.popleft()
    
    if n in save:
        continue
    else:
        save.add(n)
    
    Q.extend(graph[n])

print(len(save))
